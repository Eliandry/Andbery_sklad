from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db.models import Count, Sum
from .forms import *
from .models import Pile, NamePile, BrigadeWork, ReturnPile, Car

from django.shortcuts import render
from .models import OperationArrival, OperationDeparture


from django.http import JsonResponse
from .models import Pile
def add_beton(request):
    if request.method == "POST":
        form = BetonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BetonForm()
    return render(request, 'add_beton.html', {'form': form})

def add_wire(request):
    if request.method == "POST":
        form = WireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = WireForm()
    return render(request, 'add_wire.html', {'form': form})

def add_armature(request):
    if request.method == "POST":
        form = ArmatureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ArmatureForm()
    return render(request, 'add_armature.html', {'form': form})
def load_car_weight(request):
    car_id = request.GET.get('car_id')
    try:
        if car_id:
            car = Car.objects.get(id=car_id)
            weight = car.weight  # Предполагаем, что weight хранится в тоннах
            return JsonResponse({'weight': weight})
        else:
            return JsonResponse({'error': 'Car ID not provided'}, status=400)
    except Car.DoesNotExist:
        return JsonResponse({'error': 'Car not found'}, status=404)
def load_pile_weight(request):
    pile_id = request.GET.get('pile_id')
    try:
        if pile_id:
            pile = Pile.objects.get(id=pile_id)
            weight = pile.weight
            return JsonResponse({'weight': weight})
        else:
            # Если pile_id не предоставлен, возвращаем вес равный нулю.
            return JsonResponse({'weight': 0})
    except Pile.DoesNotExist:
        # Если свая не найдена, возвращаем ошибку или вес равный нулю.
        return JsonResponse({'error': 'Pile not found'}, status=404)
def load_brigades(request):
    type = request.GET.get('type')
    brigades = BrigadeWork.objects.filter(type=type).order_by('name')
    return JsonResponse(list(brigades.values('id', 'name')), safe=False)

def main(request):
    context = {}
    if request.user.is_authenticated:
        if request.user.userprofile.role.name == "Кладовщик":
            latest_arrivals = OperationArrival.objects.all().order_by('-date')[:10]
            latest_departures = OperationDeparture.objects.all().order_by('-date')[:10]
            context = {
                'latest_arrivals': latest_arrivals,
                'latest_departures': latest_departures,
            }
        if request.user.userprofile.role.name == "Охранник":
            departures = OperationDeparture.objects.filter(confirm=False)

            # Вычисляем общий вес для каждой отгрузки
            for departure in departures:
                departure.total_weight = departure.pile.weight * departure.quantity

            if request.method == "POST":
                departure_id = request.POST.get("departure_id")
                if departure_id:
                    departure = get_object_or_404(OperationDeparture, id=departure_id)
                    departure.confirm = True
                    departure.save()
                    return HttpResponseRedirect(reverse('main'))

            latest_confirmed_departures = OperationDeparture.objects.filter(confirm=True).order_by('-date')[:10]
            context = {
                'departures': departures,
                'confirmed': latest_confirmed_departures,
            }
        if request.user.userprofile.role.name == "Производство":
            latest_arrivals = OperationArrival.objects.all().order_by('-date')[:10]
            latest_departures = OperationDeparture.objects.all().order_by('-date')[:10]
            context = {
                'latest_arrivals': latest_arrivals,
                'latest_departures': latest_departures,
            }
    return render(request, 'main.html', context)


def operation_arrival_view(request):
    if request.user.userprofile.role.name == "Производство":
        if request.method == 'POST':
            form = OperationArrivalForm(request.POST)
            if form.is_valid():
                operation_arrival = form.save(commit=False)

                # Получаем последние цены материалов
                last_beton = Beton.objects.last()
                last_wire = Wire.objects.last()
                last_armature = Armature.objects.last()
                pile = form.cleaned_data['pile']
                quantity = form.cleaned_data['quantity']

                # Рассчитываем стоимость для каждого материала
                beton_price = pile.price_beton * quantity * (last_beton.price if last_beton else 0)
                wire_price = (pile.price_wire_3 + pile.price_wire_4 + pile.price_wire_6) * quantity * (
                    last_wire.price if last_wire else 0)
                armature_price = pile.price_armature * quantity * (last_armature.price if last_armature else 0)

                # Суммируем стоимости
                total_price = beton_price + wire_price + armature_price+(quantity*115)

                # Сохраняем рассчитанную общую цену в экземпляре
                operation_arrival.price = str(total_price)

                pile.count += quantity
                pile.defect += form.cleaned_data['defect']
                pile.save()

                operation_arrival.save()
                operation_arrival.user.add(request.user)

                # Перенаправляем на нужную страницу после сохранения
                return redirect(
                    '/operation/arrival/')  # Замените на URL, на который нужно перенаправить после успешного сохранения
        else:
            form = OperationArrivalForm()
        return render(request, 'operation_arrival.html', {'form': form})
    else:
        return redirect('/')  # или на страницу ошибки



def operation_departure_view(request):
    if request.user.userprofile.is_storekeeper:  # Проверяем, что пользователь - кладовщик
        if request.method == 'POST':
            form = OperationDepartureForm(request.POST)
            if form.is_valid():
                operation_departure = form.save(commit=False)
                pile = operation_departure.pile
                pile.count -= form.cleaned_data['quantity']

                pile.save()
                operation_departure.save()
                operation_departure.user.add(request.user)
                operation_departure.save()
                return redirect('/')  # Перенаправляем на нужную страницу после сохранения
        else:
            form = OperationDepartureForm()
        return render(request, 'operation_departure.html', {'form': form})
    else:
        return redirect('/')

from django.http import JsonResponse, HttpResponseRedirect
def get_car_numbers(request):
    brand = request.GET.get('brand')
    cars = Car.objects.filter(model=brand).values('id', 'number')
    return JsonResponse(list(cars), safe=False)


def load_piles(request):
    name_pile_id = request.GET.get('name_pile_id')
    piles = Pile.objects.filter(name_id=name_pile_id).order_by('name')
    return JsonResponse(list(piles.values('id', 'size')), safe=False)



def warehouse_statistics(request):
    piles = Pile.objects.all()
    total_count = sum(pile.count for pile in piles)
    total_defect = sum(pile.defect for pile in piles)
    pile_names = Pile.objects.values_list('name__name', flat=True).distinct()
    piles_stats = {}
    for name in pile_names:
        # Для каждого имени сваи собираем статистику по размерам
        sizes_stats = Pile.objects.filter(name__name=name).values('size').annotate(
            total_count=Sum('count'),
            total_defect=Sum('defect')
        ).order_by('size')

        piles_stats[name] = list(sizes_stats)
    context = {
        'total_count': total_count,
        'total_defect': total_defect,
        'piles_stats': piles_stats
    }
    return render(request, 'warehouse_statistics.html', context)


def return_pile_view(request):
    if request.user.userprofile.is_storekeeper:  # Проверяем, что пользователь - кладовщик
        if request.method == 'POST':
            form = ReturnPileForm(request.POST)
            if form.is_valid():
                operation_return = form.save(commit=False)
                pile = operation_return.pile
                pile.count += form.cleaned_data['quantity']
                pile.save()
                # Сохраняем объект OperationArrival перед добавлением пользователей
                operation_return.save()
                # Добавляем текущего пользователя
                operation_return.user.add(request.user)
                # Если необходимо сохранить другие изменения после добавления пользователей
                operation_return.save()
                return redirect('/')
        else:
            form = ReturnPileForm()
        return render(request, 'return_pile.html', {'form': form})
    else:
        return redirect('/')


@login_required
def operation_departure_confirm_view(request):
    if not request.user.userprofile.role.name == "Охранник":
        return redirect('/')


    departures = OperationDeparture.objects.filter(confirm=False)

    if request.method == "POST":
        departure_id = request.POST.get("departure_id")
        if departure_id:
            departure = get_object_or_404(OperationDeparture, id=departure_id)
            departure.confirm = True
            departure.save()
            return HttpResponseRedirect(reverse('main'))  # Перезагрузка страницы

    return render(request, 'main.html', {'departures': departures})





def add_pile(request):
    if request.method == 'POST':
        form = NamePileAndPileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('operation_arrival')
    else:
        form = NamePileAndPileForm()

    return render(request, 'add_pile.html', {'form': form})


def confirm_operations(request):
    if request.method == 'POST':
        operation_id = request.POST.get('operation_id')
        action = request.POST.get('action')  # Убедитесь, что action передается правильно

        operation = OperationDeparture.objects.get(id=operation_id)

        if action == 'confirm':
            operation.confirm_b = True
        elif action == 'cancel':
            operation.confirm_b = False

        operation.save()
        return redirect('confirm_operations')

    operations_to_confirm = OperationDeparture.objects.filter(confirm_b=False).order_by('-date')
    confirmed_operations = OperationDeparture.objects.filter(confirm_b=True).order_by('-date')

    context = {
        'operations_to_confirm': operations_to_confirm,
        'confirmed_operations': confirmed_operations
    }
    return render(request, 'confirm_operations.html', context)
def confirm_return_pile(request):
    if request.method == 'POST':
        return_pile_id = request.POST.get('return_pile_id')
        action = request.POST.get('action')

        return_pile = ReturnPile.objects.get(id=return_pile_id)

        if action == 'confirm':
            return_pile.confirm_b = True
        elif action == 'cancel':
            return_pile.confirm_b = False

        return_pile.save()
        return redirect('confirm_return_pile')

    return_piles_to_confirm = ReturnPile.objects.filter(confirm_b=False).order_by('-date')
    confirmed_return_piles = ReturnPile.objects.filter(confirm_b=True).order_by('-date')

    context = {
        'return_piles_to_confirm': return_piles_to_confirm,
        'confirmed_return_piles': confirmed_return_piles
    }
    return render(request, 'confirm_return_pile.html', context)

def search_departures(request):
    form = SearchForm(request.GET or None)
    results = []

    if form.is_valid():
        manager = form.cleaned_data.get('manager')
        date_from = form.cleaned_data.get('date_from')
        date_to = form.cleaned_data.get('date_to')

        queryset = OperationDeparture.objects.all()

        if manager:
            queryset = queryset.filter(manager__icontains=manager)
        if date_from:
            queryset = queryset.filter(date__gte=date_from)
        if date_to:
            queryset = queryset.filter(date__lte=date_to)

        results = queryset

    context = {
        'form': form,
        'results': results
    }

    return render(request, 'search_departures.html', context)


def search_by_date_range(request):
    form = SearchForm(request.GET or None)

    search_results = []

    if form.is_valid():
        date_from = form.cleaned_data.get('date_from')
        manager = form.cleaned_data.get('manager')
        date_to = form.cleaned_data.get('date_to')
        brigade = form.cleaned_data.get('brigade')
        departures_query = OperationDeparture.objects.all()
        arrivals_query=None
        returns_query = ReturnPile.objects.all()
        beton_query=None
        wire_query=None
        armature_query=None
        if date_from and date_to :
            departures_query = OperationDeparture.objects.filter(date__range=(date_from, date_to))
            arrivals_query = OperationArrival.objects.filter(date__range=(date_from, date_to))
            returns_query = ReturnPile.objects.filter(date__range=(date_from, date_to))
            beton_query = Beton.objects.filter(date__range=(date_from, date_to))
            wire_query = Wire.objects.filter(date__range=(date_from, date_to))
            armature_query = Armature.objects.filter(date__range=(date_from, date_to))
        if manager:
            departures_query = departures_query.filter(manager=manager)
            returns_query = returns_query.filter(manager=manager)
        if brigade and not manager:
            departures_query = departures_query.filter(brigade=brigade)
            returns_query=None
        search_results = {
                'departures': departures_query,
                'arrivals': arrivals_query,
                'returns': returns_query,
                'beton': beton_query,
                'wire': wire_query,
                'armature': armature_query
        }

    return render(request, 'search_by_date.html', {'form': form, 'search_results': search_results})

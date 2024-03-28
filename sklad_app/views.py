from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db.models import Count, Sum
from .forms import *
from .models import Pile, NamePile, BrigadeWork, ReturnPile, Car, WirehouseB

from django.shortcuts import render
from .models import OperationArrival, OperationDeparture
import json
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from .models import *


def add_beton(request):
    if request.method == "POST":
        form = BetonForm(request.POST)
        if form.is_valid():
            new_beton = form.save(commit=False)
            wirehouse, _ = WirehouseB.objects.get_or_create(id=1)  # Пример с одним складом
            wirehouse.beton += new_beton.count  # Предполагаем, что арматура используется для бетона
            wirehouse.save()
            new_beton.save()
            return redirect('/')
    else:
        form = BetonForm()
    return render(request, 'add_beton.html', {'form': form})


def classif(request):
    return render(request, 'classes.html')


def add_wire(request):
    if request.method == "POST":
        form = WireForm(request.POST)
        if form.is_valid():
            new_wire = form.save(commit=False)
            wirehouse, _ = WirehouseB.objects.get_or_create(id=1)
            wirehouse.wire3 += new_wire.count
            wirehouse.save()
            new_wire.save()
            return redirect('/')
    else:
        form = WireForm()
    return render(request, 'add_wire.html', {'form': form})



def add_wire4(request):
    if request.method == "POST":
        form = WireForm4(request.POST)
        if form.is_valid():
            new_wire = form.save(commit=False)
            wirehouse, _ = WirehouseB.objects.get_or_create(id=1)
            wirehouse.wire4 += new_wire.count
            wirehouse.save()
            new_wire.save()
            return redirect('/')
    else:
        form = WireForm()
    return render(request, 'add_wire.html', {'form': form})


def add_wire6(request):
    if request.method == "POST":
        form = WireForm6(request.POST)
        if form.is_valid():
            new_wire = form.save(commit=False)
            wirehouse, _ = WirehouseB.objects.get_or_create(id=1)
            wirehouse.wire6 += new_wire.count
            wirehouse.save()
            new_wire.save()
            return redirect('/')
    else:
        form = WireForm()
    return render(request, 'add_wire.html', {'form': form})


def add_armature(request):
    if request.method == "POST":
        form = ArmatureForm(request.POST)
        if form.is_valid():
            new_arm = form.save(commit=False)
            wirehouse, _ = WirehouseB.objects.get_or_create(id=1)  # Пример с одним складом
            wirehouse.armature += new_arm.count  # Предполагаем, что арматура используется для бетона
            wirehouse.save()
            new_arm.save()
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
            for arrival in latest_arrivals:
                if arrival.details:
                    details = json.loads(arrival.details)
                    arrival.piles_info = []
                    for detail in details:
                        try:
                            pile = Pile.objects.get(id=detail["pile_id"])
                            arrival.piles_info.append({
                                "pile": pile,
                                "quantity": detail["quantity"]
                            })
                        except Pile.DoesNotExist:
                            continue
            latest_departures = OperationDeparture.objects.all().order_by('-date')[:10]
            for departure in latest_departures:
                if departure.details:
                    details = json.loads(departure.details)
                    departure.piles_info = []
                    for detail in details:
                        try:
                            pile = Pile.objects.get(id=detail["pile_id"])
                            departure.piles_info.append({
                                "pile": pile,
                                "quantity": detail["quantity"]
                            })
                        except Pile.DoesNotExist:
                            continue
            context = {
                'latest_arrivals': latest_arrivals,
                'latest_departures': latest_departures,
            }
        if request.user.userprofile.role.name == "Охранник":
            departures = OperationDeparture.objects.filter(confirm=False)
            for departure in departures:
                if departure.details:
                    details = json.loads(departure.details)
                    departure.piles_info = []
                    for detail in details:
                        try:
                            pile = Pile.objects.get(id=detail["pile_id"])
                            departure.piles_info.append({
                                "pile": pile,
                                "quantity": detail["quantity"]
                            })
                        except Pile.DoesNotExist:
                            continue


            if request.method == "POST":
                departure_id = request.POST.get("departure_id")
                if departure_id:
                    departure = get_object_or_404(OperationDeparture, id=departure_id)
                    departure.confirm = True
                    departure.save()
                    return HttpResponseRedirect(reverse('main'))

            latest_confirmed_departures = OperationDeparture.objects.filter(confirm=True).order_by('-date')[:10]
            for departure in latest_confirmed_departures:
                if departure.details:
                    details = json.loads(departure.details)
                    departure.piles_info = []
                    for detail in details:
                        try:
                            pile = Pile.objects.get(id=detail["pile_id"])
                            departure.piles_info.append({
                                "pile": pile,
                                "quantity": detail["quantity"]
                            })
                        except Pile.DoesNotExist:
                            continue
            context = {
                'departures': departures,
                'confirmed': latest_confirmed_departures,
            }
        if request.user.userprofile.role.name == "Производство":

            latest_arrivals = OperationArrival.objects.all().order_by('-date')[:10]
            for arrival in latest_arrivals:
                if arrival.details:
                    details = json.loads(arrival.details)
                    arrival.piles_info = []
                    for detail in details:
                        try:
                            pile = Pile.objects.get(id=detail["pile_id"])
                            arrival.piles_info.append({
                                "pile": pile,
                                "quantity": detail["quantity"]
                            })
                        except Pile.DoesNotExist:
                            continue
            latest_departures = OperationDeparture.objects.all().order_by('-date')[:10]
            for departure in latest_departures:
                if departure.details:
                    details = json.loads(departure.details)
                    departure.piles_info = []
                    for detail in details:
                        try:
                            pile = Pile.objects.get(id=detail["pile_id"])
                            departure.piles_info.append({
                                "pile": pile,
                                "quantity": detail["quantity"]
                            })
                        except Pile.DoesNotExist:
                            continue
            today = timezone.now().date()
            try:
                # Получаем последний заказ за сегодня
                order = Order.objects.filter(date__date=today).latest(
                    'date')  # Предполагается, что в модели Order есть поле date
            except Order.DoesNotExist:
                order = None

            if order:
                # Преобразуем данные о сваях из JSON в словарь
                piles_info = json.loads(order.piles_info)
                materials_total = {
                    'total_beton': order.total_beton,
                    'total_wire_3': order.total_wire_3,
                    'total_wire_4': order.total_wire_4,
                    'total_wire_6': order.total_wire_6,
                    'total_armature': order.total_armature
                }
            else:
                piles_info = {}
                materials_total = {}
            context = {
                'latest_arrivals': latest_arrivals,
                'latest_departures': latest_departures,
                'piles_info': piles_info,
                'materials_total': materials_total
            }
    return render(request, 'main.html', context)


def operation_arrival_view(request):
    piles = Pile.objects.filter(name__pile_type='жб')
    brigades = Brigade.objects.all()

    if request.method == 'POST':
        brigade_id = request.POST.get('brigade')
        brigade = Brigade.objects.get(id=brigade_id)

        wirehouse, _ = WirehouseB.objects.get_or_create(id=1)
        # Получаем последние цены материалов
        last_beton = Beton.objects.last()
        last_wire = Wire.objects.last()
        last_wire4 = Wire4.objects.last()
        last_wire6 = Wire6.objects.last()
        last_armature = Armature.objects.last()

        total_price = 0
        piles_info = []
        for key, value in request.POST.items():
            if key.startswith('pile_') and value:
                pile_id = key.split('_')[1]
                pile = Pile.objects.get(pk=pile_id)

                quantity = int(value)
                pile.count+=quantity
                pile.save()
                if quantity > 0:
                    piles_info.append({"pile_id": pile.id, "quantity": quantity})
                    # Рассчитываем стоимость для каждого материала
                    b_count = pile.price_beton * quantity
                    w3_count = pile.price_wire_3 * quantity
                    w4_count = pile.price_wire_4 * quantity
                    w6_count = pile.price_wire_6 * quantity
                    arm_count = pile.price_armature * quantity

                    beton_price = b_count * (last_beton.price if last_beton else 0)
                    wire3_price = w3_count * (last_wire.price if last_wire else 0)
                    wire4_price = w4_count * (last_wire4.price if last_wire4 else 0)
                    wire6_price = w6_count * (last_wire6.price if last_wire6 else 0)
                    armature_price = arm_count * (last_armature.price if last_armature else 0)

                    # Суммируем стоимости
                    total_price += beton_price + wire3_price + wire4_price + wire6_price + armature_price

        # Обновляем количество материалов на складе
        wirehouse.wire3 -= sum(item["quantity"] * pile.price_wire_3 for item in piles_info)
        wirehouse.wire4 -= sum(item["quantity"] * pile.price_wire_4 for item in piles_info)
        wirehouse.wire6 -= sum(item["quantity"] * pile.price_wire_6 for item in piles_info)
        wirehouse.armature -= sum(item["quantity"] * pile.price_armature for item in piles_info)
        wirehouse.beton -= sum(item["quantity"] * pile.price_beton for item in piles_info)
        wirehouse.save()

        # Создаем операцию прихода со всей информацией о сваях
        operation_arrival=OperationArrival.objects.create(
            details=json.dumps(piles_info),
            brigade=brigade,
            price=str(total_price),
        )
        operation_arrival.user.add(request.user)
        operation_arrival.save()
        return redirect('/')

    return render(request, 'operation_arrival.html', {'piles': piles, 'brigades': brigades})


def operation_departure_view(request):
    if request.method == 'POST':
        manager = request.POST.get('manager')
        description = request.POST.get('description')
        number_car_id = request.POST.get('number_car')
        brigade_id = request.POST.get('brigade')  # Получение ID выбранной бригады
        details_list = []

        # Итерация по всем полученным данным формы
        for key, value in request.POST.items():
            if key.startswith('pile_') and value:  # Проверка, принадлежит ли ключ к Pile и не пустое ли значение
                quantity = int(value)  # Преобразование введенного значения в число
                if quantity > 0:  # Проверка, что количество больше нуля
                    pile_id = key.split('_')[1]
                    pile=Pile.objects.get(id=int(pile_id))
                    pile.count-=int(quantity)
                    pile.save()
                    details_list.append({"pile_id": pile_id, "quantity": quantity})

        if not details_list:  # Если список деталей пуст, возвращаем ошибку
            return HttpResponse("Пожалуйста, введите количество для хотя бы одной сваи.", status=400)

        details = json.dumps(details_list)  # Преобразование списка деталей в JSON строку

        operation_departure = OperationDeparture(
            manager=manager,
            description=description,
            details=details,
            number_car=Car.objects.get(number=number_car_id) if number_car_id else None,
            brigade=BrigadeWork.objects.get(id=brigade_id) if brigade_id else None,
        )
        operation_departure.save()

        # Обработка и сохранение связей ManyToMany, если необходимо

        return redirect('/')  # Перенаправление после сохранения
    else:
        piles = Pile.objects.filter(name__pile_type='жб')  # Получаем все объекты Pile для формы
        cars = Car.objects.all()  # Получаем все объекты Car для выбора
        brigades = BrigadeWork.objects.filter(type='жб')  # Получение всех объектов BrigadeWork для выбора
        return render(request, 'operation_departure.html', {'piles': piles, 'cars': cars, 'brigades': brigades,'car_type_choices': Car.TYPE_CHOICES,})





def get_car_numbers(request):
    model = request.GET.get('model')
    numbers = list(Car.objects.filter(model=model).values_list('number', flat=True))
    return JsonResponse({'numbers': numbers})


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
        latest_arrivals = None
        returns_query = ReturnPile.objects.all()
        beton_query = None
        wire_query = None
        armature_query = None
        order_query=None
        if date_from and date_to:
            order_query=Order.objects.filter(date__range=(date_from, date_to))
            departures_query = OperationDeparture.objects.filter(date__range=(date_from, date_to))
            latest_arrivals = OperationArrival.objects.filter(date__range=(date_from, date_to))
            returns_query = ReturnPile.objects.filter(date__range=(date_from, date_to))
            beton_query = Beton.objects.filter(date__range=(date_from, date_to))
            wire_query = Wire.objects.filter(date__range=(date_from, date_to))
            armature_query = Armature.objects.filter(date__range=(date_from, date_to))
        if manager:
            departures_query = departures_query.filter(manager=manager)
            returns_query = returns_query.filter(manager=manager)
        if brigade and not manager:
            departures_query = departures_query.filter(brigade=brigade)
            returns_query = None
        for arrival in latest_arrivals:
            if arrival.details:
                details = json.loads(arrival.details)
                arrival.piles_info = []
                for detail in details:
                    try:
                        pile = Pile.objects.get(id=detail["pile_id"])
                        arrival.piles_info.append({
                            "pile": pile,
                            "quantity": detail["quantity"]
                        })
                    except Pile.DoesNotExist:
                        continue
        for arrival in departures_query:
            if arrival.details:
                details = json.loads(arrival.details)
                arrival.piles_info = []
                for detail in details:
                    try:
                        pile = Pile.objects.get(id=detail["pile_id"])
                        arrival.piles_info.append({
                            "pile": pile,
                            "quantity": detail["quantity"]
                        })
                    except Pile.DoesNotExist:
                        continue
        search_results = {
            'departures': departures_query,
            'arrivals': latest_arrivals,
            'returns': returns_query,
            'beton': beton_query,
            'wire': wire_query,
            'armature': armature_query,
            'order':order_query
        }

    return render(request, 'search_by_date.html', {'form': form, 'search_results': search_results})


from django.shortcuts import render
from .models import Beton, Wire, Wire4, Wire6, Armature, WirehouseB


def materials_overview(request):
    # Получаем 5 последних записей для каждого типа материала
    last_five_beton = Beton.objects.all().order_by('-date')[:5]
    last_five_wire = Wire.objects.all().order_by('-date')[:5]
    last_five_wire4 = Wire4.objects.all().order_by('-date')[:5]
    last_five_wire6 = Wire6.objects.all().order_by('-date')[:5]
    last_five_armature = Armature.objects.all().order_by('-date')[:5]

    # Предполагаем, что у нас есть только один экземпляр WirehouseB
    wirehouseb = WirehouseB.objects.first()

    context = {
        'last_five_beton': last_five_beton,
        'last_five_wire': last_five_wire,
        'last_five_wire4': last_five_wire4,
        'last_five_wire6': last_five_wire6,
        'last_five_armature': last_five_armature,
        'wirehouseb': wirehouseb,
    }
    return render(request, 'materials_overview.html', context)


from django.shortcuts import render
from .models import Pile, Order


def create_order(request):
    if request.method == "POST":
        piles = Pile.objects.filter(name__pile_type='жб')

        total_beton = 0
        total_wire_3 = 0
        total_wire_4 = 0
        total_wire_6 = 0
        total_armature = 0
        piles_info = {}  # Обновленный словарь для хранения информации о сваях

        for pile in piles:
            quantity = request.POST.get(f'pile_{pile.id}', 0)
            if quantity:
                quantity = int(quantity)
                if quantity > 0:  # Добавляем в словарь только если количество больше 0
                    pile_key = f"{pile.name.name} {pile.size}"  # Используем имя и размер для ключа
                    piles_info[pile_key] = quantity
                    total_beton += pile.price_beton * quantity
                    total_wire_3 += pile.price_wire_3 * quantity
                    total_wire_4 += pile.price_wire_4 * quantity
                    total_wire_6 += pile.price_wire_6 * quantity
                    total_armature += pile.price_armature * quantity

        # Проверяем, были ли добавлены сваи в заказ
        if piles_info:
            order = Order(
                piles_info=json.dumps(piles_info),  # Сериализация обновленного словаря в JSON строку
                total_beton=total_beton,
                total_wire_3=total_wire_3,
                total_wire_4=total_wire_4,
                total_wire_6=total_wire_6,
                total_armature=total_armature
            )
            order.save()

            return redirect('/')
        else:
            # Если сваи не были добавлены, возможно, стоит добавить сообщение об ошибке
            return render(request, 'create_order.html', {'piles': piles, 'error': 'No piles were selected.'})

    else:
        piles = Pile.objects.filter(name__pile_type='жб')
        return render(request, 'create_order.html', {'piles': piles})








#Винты
def materialsV_overview(request):
    # Получаем 5 последних записей для каждого типа материала

    # Предполагаем, что у нас есть только один экземпляр WirehouseB
    wirehousev = WirehouseV.objects.first()

    context = {

        'wirehousev': wirehousev,
    }
    return render(request, 'materials_v.html', context)

def add_tube(request):
    if request.method == "POST":
        form = TubeForm(request.POST)
        if form.is_valid():
            new_wire = form.save(commit=False)
            wirehouse, _ = WirehouseV.objects.get_or_create(id=1)
            wirehouse.tube += new_wire.count
            wirehouse.save()
            new_wire.save()
            return redirect('/')
    else:
        form = WireForm()
    return render(request, 'add_tube.html', {'form': form})

def add_lists(request):
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            new_wire = form.save(commit=False)
            wirehouse, _ = WirehouseV.objects.get_or_create(id=1)
            wirehouse.lists += new_wire.count
            wirehouse.save()
            new_wire.save()
            return redirect('/')
    else:
        form = WireForm()
    return render(request, 'add_list.html', {'form': form})





def calculate_lopasti(request):
    if request.method == 'POST':
        details = []
        total_lopasti = 0
        price_per_unit = 0
        wirehouse_v, _ = WirehouseV.objects.get_or_create(id=1)
        # Соответствие между диаметрами листов и количеством лопастей, которое можно получить
        lopasti_per_sheet = {89: 66, 108: 56, 133: 39}

        for diameter, multiplier in lopasti_per_sheet.items():
            sheet_count = int(request.POST.get(str(diameter), 0))
            if sheet_count > 0:
                lopasti_count = sheet_count * multiplier
                total_lopasti += lopasti_count

                # Находим последний добавленный лист соответствующего размера и его цену
                last_list = Lists.objects.last()
                if last_list:
                    price_per_unit = round(last_list.price / multiplier, 2)

                if diameter == 89:
                    wirehouse_v.lopasti89 += lopasti_count
                elif diameter == 108:
                    wirehouse_v.lopasti108 += lopasti_count
                elif diameter == 133:
                    wirehouse_v.lopasti133 += lopasti_count

                    # Уменьшаем количество листов на складе
                wirehouse_v.lists -= sheet_count
                details.append({
                    "diameter": diameter,
                    "lopasti_count": lopasti_count,
                    "price_per_unit": price_per_unit
                })
        wirehouse_v.save()
        # Сохраняем результат в модели Lopasti
        Lopasti.objects.create(details=json.dumps(details))

        return redirect('/')  # Измените на ваш URL для перенаправления
    else:
        return render(request, 'lopasti_calculation.html')  # Измените на ваш шаблон ввода данных
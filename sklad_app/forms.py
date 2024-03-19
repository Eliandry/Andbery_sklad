from .models import OperationArrival, BrigadeWork, Car
from django import forms
from .models import OperationDeparture, NamePile, Pile, ReturnPile
from .models import Beton, Wire, Armature


class BetonForm(forms.ModelForm):
    class Meta:
        model = Beton
        exclude = ['date']  # Исключаем поле даты
        labels = {
            'count': 'Количество',
            'company_sell': 'Компания-продавец',
            'company_buy': 'Компания-покупатель',
            'price': 'Цена',
        }

class WireForm(forms.ModelForm):
    class Meta:
        model = Wire
        exclude = ['date']  # Исключаем поле даты
        labels = {
            'count': 'Количество',
            'company_sell': 'Компания-продавец',
            'company_buy': 'Компания-покупатель',
            'price': 'Цена',
        }

class ArmatureForm(forms.ModelForm):
    class Meta:
        model = Armature
        exclude = ['date']  # Исключаем поле даты
        labels = {
            'count': 'Количество',
            'company_sell': 'Компания-продавец',
            'company_buy': 'Компания-покупатель',
            'price': 'Цена',
        }


class OperationArrivalForm(forms.ModelForm):
    name_pile = forms.ModelChoiceField(queryset=NamePile.objects.all(), label="Название сваи", required=True)

    class Meta:
        model = OperationArrival
        fields = ['name_pile', 'pile', 'quantity', 'defect', 'description', 'brigade']
        labels = {
            'name_pile': 'Название сваи',
            'pile': 'Свая',
            'quantity': 'Количество',
            'defect': 'Дефекты',
            'description': 'Описание (если требуется)',
            'brigade': 'Бригада',
        }
        widgets = {
            'name_pile': forms.Select(attrs={'class': 'name_pile'}),
            'pile': forms.Select(attrs={'class': 'pile'}),
        }

    def __init__(self, *args, **kwargs):
        super(OperationArrivalForm, self).__init__(*args, **kwargs)
        self.fields['pile'].queryset = Pile.objects.none()

        if 'name_pile' in self.data:
            try:
                name_pile_id = int(self.data.get('name_pile'))
                self.fields['pile'].queryset = Pile.objects.filter(name_id=name_pile_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['pile'].queryset = self.instance.name_pile.pile_set.order_by('name')



class OperationDepartureForm(forms.ModelForm):
    name_pile = forms.ModelChoiceField(queryset=NamePile.objects.all(), label="Название сваи", required=True)
    type_brigade = forms.ChoiceField(choices=BrigadeWork.TYPE_CHOICES, label="Тип бригады", required=True)
    car_brand = forms.ChoiceField(choices=Car.TYPE_CHOICES, label="Марка автомобиля", required=True)

    class Meta:
        model = OperationDeparture
        fields = ['manager', 'name_pile', 'pile', 'quantity', 'description', 'car_brand', 'number_car', 'type_brigade','brigade']
        labels = {
            'manager': 'Лид',
            'name_pile': 'Название сваи',
            'pile': 'Свая',
            'quantity': 'Количество',
            'description': 'Описание (если требуется)',
            'car_brand': 'Марка автомобиля',
            'number_car': 'Автомобиль',
            'brigade': 'Бригада',
        }

    def __init__(self, *args, **kwargs):
        super(OperationDepartureForm, self).__init__(*args, **kwargs)

        self.fields['pile'].queryset = Pile.objects.none()
        self.order_fields(['name_pile', 'pile', 'quantity', 'description', 'type_brigade', 'brigade', 'number_car'])
        if 'name_pile' in self.data:
            try:
                name_pile_id = int(self.data.get('name_pile'))
                self.fields['pile'].queryset = Pile.objects.filter(name_id=name_pile_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['pile'].queryset = self.instance.name_pile.pile_set.order_by('name')

        super(OperationDepartureForm, self).__init__(*args, **kwargs)

        self.fields['number_car'].queryset = Car.objects.none()

        if 'car_brand' in self.data:
            try:
                car_brand = self.data.get('car_brand')
                self.fields['number_car'].queryset = Car.objects.filter(model=car_brand).order_by('number')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['number_car'].queryset = self.instance.car_brand.car_set.order_by('number')


class ReturnPileForm(forms.ModelForm):
    name_pile = forms.ModelChoiceField(queryset=NamePile.objects.all(), label="Название сваи", required=True)

    class Meta:
        model = ReturnPile
        fields = ['name_pile', 'pile', 'quantity', 'description']
        labels = {
            'name_pile': 'Название сваи',
            'pile': 'Свая',
            'quantity': 'Количество',
            'description': 'Описание (если требуется)',
        }

    def __init__(self, *args, **kwargs):
        super(ReturnPileForm, self).__init__(*args, **kwargs)
        self.fields['pile'].queryset = Pile.objects.none()

        if 'name_pile' in self.data:
            try:
                name_pile_id = int(self.data.get('name_pile'))
                self.fields['pile'].queryset = Pile.objects.filter(name_id=name_pile_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['pile'].queryset = self.instance.name_pile.pile_set.order_by('name')


class SearchForm(forms.Form):
    manager = forms.CharField(max_length=500, required=False, label='Лид')
    date_from = forms.DateField(required=False, label='Дата с', widget=forms.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(required=False, label='Дата по', widget=forms.DateInput(attrs={'type': 'date'}))
    brigade = forms.ModelChoiceField(queryset=BrigadeWork.objects.all(), required=False, empty_label="Все бригады",label='Бригада')


class NamePileAndPileForm(forms.Form):
    name = forms.CharField(max_length=232, label="Название")
    pile_type = forms.ChoiceField(choices=NamePile.TYPE_CHOICES, label="Тип")
    size = forms.CharField(max_length=100, label="Размер")
    count = forms.IntegerField(label="Количество")
    defect = forms.IntegerField(label="Дефекты")

    def save(self):
        name_pile_data = {
            'name': self.cleaned_data['name'],
            'pile_type': self.cleaned_data['pile_type']
        }
        name_pile = NamePile.objects.create(**name_pile_data)

        pile_data = {
            'name': name_pile,
            'size': self.cleaned_data['size'],
            'count': self.cleaned_data['count'],
            'defect': self.cleaned_data['defect']
        }
        Pile.objects.create(**pile_data)


class DateRangeForm(forms.Form):
    date_from = forms.DateField(required=False, label='Дата с', widget=forms.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(required=False, label='Дата по', widget=forms.DateInput(attrs={'type': 'date'}))
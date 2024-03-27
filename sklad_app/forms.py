from .models import OperationArrival, BrigadeWork, Car
from django import forms

from .models import *


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
class WireForm4(forms.ModelForm):
    class Meta:
        model = Wire4
        exclude = ['date']  # Исключаем поле даты
        labels = {
            'count': 'Количество',
            'company_sell': 'Компания-продавец',
            'company_buy': 'Компания-покупатель',
            'price': 'Цена',
        }
class WireForm6(forms.ModelForm):
    class Meta:
        model = Wire6
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

class TubeForm(forms.ModelForm):
    class Meta:
        model = Tube
        exclude = ['date']  # Исключаем поле даты
        labels = {
            'count': 'Количество',
            'company_sell': 'Компания-продавец',
            'company_buy': 'Компания-покупатель',
            'price': 'Цена',
        }
class ListForm(forms.ModelForm):
    class Meta:
        model = Lists
        exclude = ['date']  # Исключаем поле даты
        labels = {
            'count': 'Количество',
            'company_sell': 'Компания-продавец',
            'company_buy': 'Компания-покупатель',
            'price': 'Цена',
        }








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
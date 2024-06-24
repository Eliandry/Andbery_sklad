from .models import OperationArrival, BrigadeWork, Car
from django import forms
from .models import OperationDeparture, NamePile, Pile, ReturnPile
from .models import *


class BetonForm(forms.ModelForm):
    class Meta:
        model = Beton
        exclude = ['date']  # Исключаем поле даты
        labels = {
            'count': 'Количество в куб',
            'company_sell': 'Компания-продавец',
            'company_buy': 'Компания-покупатель',
            'price': 'Цена за куб',
        }

class WireForm(forms.ModelForm):
    class Meta:
        model = Wire
        exclude = ['date']  # Исключаем поле даты
        labels = {
            'count': 'Количество',
            'company_sell': 'Компания-продавец',
            'company_buy': 'Компания-покупатель',
            'price': 'Цена за кг',
        }
class WireForm4(forms.ModelForm):
    class Meta:
        model = Wire4
        exclude = ['date']  # Исключаем поле даты
        labels = {
            'count': 'Количество',
            'company_sell': 'Компания-продавец',
            'company_buy': 'Компания-покупатель',
            'price': 'Цена за кг',
        }
class WireForm6(forms.ModelForm):
    class Meta:
        model = Wire6
        exclude = ['date']  # Исключаем поле даты
        labels = {
            'count': 'Количество',
            'company_sell': 'Компания-продавец',
            'company_buy': 'Компания-покупатель',
            'price': 'Цена за кг',
        }
class ArmatureForm(forms.ModelForm):
    class Meta:
        model = Armature
        exclude = ['date']  # Исключаем поле даты
        labels = {
            'count': 'Количество в кг',
            'company_sell': 'Компания-продавец',
            'company_buy': 'Компания-покупатель',
            'price': 'Цена за кг',
        }
class Armature10Form(forms.ModelForm):
    class Meta:
        model = Armature10
        exclude = ['date']  # Исключаем поле даты
        labels = {
            'count': 'Количество в кг',
            'company_sell': 'Компания-продавец',
            'company_buy': 'Компания-покупатель',
            'price': 'Цена за кг',
        }

#class OperationArrivalForm(forms.ModelForm):
#    name_pile = forms.ModelChoiceField(queryset=NamePile.objects.all(), label="Название сваи", required=True)
#
#    class Meta:
 #       model = OperationArrival
 #       fields = ['name_pile', 'pile', 'quantity', 'description', 'brigade']
  #      labels = {
   #         'name_pile': 'Название сваи',
    #        'pile': 'Свая',
    #        'quantity': 'Количество',
     #       'description': 'Описание (если требуется)',
      #      'brigade': 'Бригада',
       # }
        #widgets = {
    #        'name_pile': forms.Select(attrs={'class': 'name_pile'}),
     #       'pile': forms.Select(attrs={'class': 'pile'}),
      #  }

#    def __init__(self, *args, **kwargs):
 #       super(OperationArrivalForm, self).__init__(*args, **kwargs)
  #      self.fields['pile'].queryset = Pile.objects.none()
#
 #       if 'name_pile' in self.data:
  #          try:
   #             name_pile_id = int(self.data.get('name_pile'))
    #            self.fields['pile'].queryset = Pile.objects.filter(name_id=name_pile_id).order_by('name')
     #       except (ValueError, TypeError):
      #          pass  # invalid input from the client; ignore and fallback to empty City queryset
       # elif self.instance.pk:
        #    self.fields['pile'].queryset = self.instance.name_pile.pile_set.order_by('name')






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




class TubeForm(forms.ModelForm):
    class Meta:
        model = Tube
        exclude = ['date','unit_price']
        labels = {
            'count': 'Кг 89 трубы',
            'company_sell': 'Компания-продавец',
            'company_buy': 'Компания-покупатель',
            'price': 'Стоимость',
        }
class TubeForm108(forms.ModelForm):
    class Meta:
        model = Tube108
        exclude = ['date','unit_price']  # Исключаем поле даты
        labels = {
            'count': 'Кг 108 трубы',
            'company_sell': 'Компания-продавец',
            'company_buy': 'Компания-покупатель',
            'price': 'Стоимость',
        }
class TubeForm108_2(forms.ModelForm):
    class Meta:
        model = Tube108_2
        exclude = ['date','unit_price']
        labels = {
            'count': 'Кг 108*3.5 трубы',
            'company_sell': 'Компания-продавец',
            'company_buy': 'Компания-покупатель',
            'price': 'Стоимость',
        }
class TubeForm133(forms.ModelForm):
    class Meta:
        model = Tube133
        exclude = ['date','unit_price']
        labels = {
            'count': 'Кг 133 трубы',
            'company_sell': 'Компания-продавец',
            'company_buy': 'Компания-покупатель',
            'price': 'Стоимость',
        }
class ListForm(forms.ModelForm):
    class Meta:
        model = Lists
        fields = ['count', 'company_sell', 'company_buy', 'price']
        labels = {
            'count': 'Количество',
            'company_sell': 'Компания-продавец',
            'company_buy': 'Компания-покупатель',
            'price': 'Цена',
        }

class List5Form(forms.ModelForm):
    class Meta:
        model = Lists5
        fields = ['count', 'company_sell', 'company_buy', 'price']
        labels = {
            'count': 'Количество',
            'company_sell': 'Компания-продавец',
            'company_buy': 'Компания-покупатель',
            'price': 'Цена',
        }

class ExportForm(forms.Form):
    date_from = forms.DateField(label='Дата с', widget=forms.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(label='Дата по', widget=forms.DateInput(attrs={'type': 'date'}))
    brigade = forms.ModelChoiceField(label='Бригада', queryset=BrigadeWork.objects.all(), required=False)

class ExportArrForm(forms.Form):
    date_from = forms.DateField(label='Дата с', widget=forms.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(label='Дата по', widget=forms.DateInput(attrs={'type': 'date'}))
    brigade = forms.ModelChoiceField(label='Бригада', queryset=Brigade.objects.all(), required=False)

from django.forms import ModelChoiceField, DateField

class MaterialExportForm(forms.Form):
    MATERIAL_CHOICES = [
        ('beton', 'Бетон'),
        ('wire', 'Проволка 3мм'),
        ('wire4', 'Проволка 4мм'),
        ('wire6', 'Проволка 6мм'),
        ('armature', 'Арматура 8мм'),
        ('armature10', 'Арматура 10мм')
    ]
    material = forms.ChoiceField(choices=MATERIAL_CHOICES, label="Select Material")
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="From")
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="To")

class TextProcessingForm(forms.Form):
    text_input = forms.CharField(label='Введите смс', widget=forms.Textarea)
    brigade = forms.ModelChoiceField(queryset=BrigadeWork.objects.all(), label='Выберите бригаду', required=False)

class AddPileForm(forms.Form):
    pile = forms.ChoiceField(label='Выберите сваю')
    quantity = forms.IntegerField(label='Количество', min_value=1)

class ToolOperationForm(forms.Form):
    brigade = forms.ModelChoiceField(queryset=BrigadeWork.objects.all(), label='Выберите бригаду')
    operation = forms.ChoiceField(choices=[('Списать', 'Списать'), ('Дать', 'Дать')], label='Выберите операцию')

    def __init__(self, *args, **kwargs):
        super(ToolOperationForm, self).__init__(*args, **kwargs)
        tools = Tool.objects.all()
        for tool in tools:
            self.fields[f'tool_{tool.id}'] = forms.IntegerField(label=f'{tool.name}', min_value=0, required=False)

class DateRangeForm(forms.Form):
    start_date = forms.DateField(label='Дата начала', widget=forms.TextInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label='Дата окончания', required=False, widget=forms.TextInput(attrs={'type': 'date'}))
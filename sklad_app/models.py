from django.db import models
from django.contrib.auth.models import User
from django.forms import JSONField


# Create your models here.
class Brigade(models.Model):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name


class Car(models.Model):
    TYPE_CHOICES = (
        ('Неизвестно', 'Неизвестно'),
        ('Маз', 'Маз'),
        ('Камаз', 'Камаз'),
        ('Хино', 'Хино'),
        ('FAW', 'FAW'),
        ('Мерседес', 'Мерседес')
    )
    model = models.CharField(max_length=30, choices=TYPE_CHOICES)
    number = models.CharField(max_length=123)
    weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0.0)

    def __str__(self):
        return self.number


class BrigadeWork(models.Model):
    name = models.CharField(max_length=123)
    TYPE_CHOICES = (
        ('винты', 'Винты'),
        ('жб', 'ЖБ'),
        ('ручники', 'Ручники'),

    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='жб', verbose_name='Тип')

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class NamePile(models.Model):
    TYPE_CHOICES = (
        ('винтовые', 'Винтовые'),
        ('жб', 'Железобетонные'),
    )

    name = models.CharField(max_length=232)
    pile_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='винтовые', verbose_name='Тип')

    def __str__(self):
        return f"{self.name} ({self.pile_type})"


class Beton(models.Model):
    count = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    company_sell = models.CharField(max_length=200)
    company_buy = models.CharField(max_length=200)
    price = models.IntegerField()



class WirehouseB(models.Model):
    beton = models.IntegerField(default=0)
    armature = models.IntegerField(default=0)
    wire3 = models.IntegerField(default=0)
    wire4 = models.IntegerField(default=0)
    wire6 = models.IntegerField(default=0)

class WirehouseV(models.Model):
    lopasti89 = models.IntegerField(default=0)
    lopasti108 = models.IntegerField(default=0)
    lopasti133 = models.IntegerField(default=0)
    lists = models.IntegerField(default=0)
    tube = models.IntegerField(default=0)



class Wire(models.Model):
    count = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    company_sell = models.CharField(max_length=200)
    company_buy = models.CharField(max_length=200)
    price = models.IntegerField()


class Wire4(models.Model):
    count = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    company_sell = models.CharField(max_length=200)
    company_buy = models.CharField(max_length=200)
    price = models.IntegerField()


class Wire6(models.Model):
    count = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    company_sell = models.CharField(max_length=200)
    company_buy = models.CharField(max_length=200)
    price = models.IntegerField()


class Armature(models.Model):
    count = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    company_sell = models.CharField(max_length=200)
    company_buy = models.CharField(max_length=200)
    price = models.IntegerField()

class Tube(models.Model):
    count = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    company_sell = models.CharField(max_length=200)
    company_buy = models.CharField(max_length=200)
    price = models.IntegerField()

class Lists(models.Model):
    count = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    company_sell = models.CharField(max_length=200)
    company_buy = models.CharField(max_length=200)
    price = models.IntegerField()

class Lopasti(models.Model):
    details = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


class Pile(models.Model):
    name = models.ForeignKey(NamePile, on_delete=models.CASCADE)
    size = models.CharField(max_length=100)
    weight = models.IntegerField(default=0)
    price_beton = models.DecimalField(max_digits=10, decimal_places=4, blank=True, default=0.0)
    price_wire_3 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, default=0.0)
    price_wire_4 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, default=0.0)
    price_wire_6 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, default=0.0)
    price_armature = models.DecimalField(max_digits=10, decimal_places=4, blank=True, default=0.0)
    to_lopast=models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    defect = models.IntegerField(default=0)

    def __str__(self):
        return self.size


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    @property
    def is_storekeeper(self):
        return self.role.name == "Кладовщик"


class OperationArrival(models.Model):
    details = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ManyToManyField(User)
    confirm_b = models.BooleanField(default=False)
    description = models.CharField(blank=True, max_length=500)
    defect = models.IntegerField(blank=True, default=0)
    brigade = models.ForeignKey(Brigade, on_delete=models.CASCADE)
    price = models.CharField(max_length=200, default=0)


class OperationDeparture(models.Model):
    manager = models.CharField(max_length=500, default='123')
    details = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ManyToManyField(User)
    description = models.CharField(blank=True, max_length=500)
    confirm = models.BooleanField(default=False)
    number_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    brigade = models.ForeignKey(BrigadeWork, on_delete=models.CASCADE, blank=True)
    confirm_b = models.BooleanField(default=False)
    confirm_bb = models.BooleanField(default=False)


class ReturnPile(models.Model):
    manager = models.CharField(max_length=500, default='123')
    pile = models.ForeignKey(Pile, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    description = models.CharField(blank=True, max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ManyToManyField(User)
    confirm_b = models.BooleanField(default=False)

class Order(models.Model):
    piles_info = models.TextField()  # Сохраняем информацию о сваях и количествах в текстовом формате
    total_beton = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_wire_3 = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_wire_4 = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_wire_6 = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_armature = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    date = models.DateTimeField(auto_now_add=True)

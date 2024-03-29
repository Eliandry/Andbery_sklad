from django.contrib import admin
from .models import Brigade, BrigadeWork, Role, NamePile, Pile, UserProfile, OperationArrival, OperationDeparture, \
    ReturnPile, Car, WirehouseB, Order, WirehouseV, Tube, Lists, Lopasti

from .models import Beton, Wire, Armature

@admin.register(Beton)
class BetonAdmin(admin.ModelAdmin):
    list_display = ('count', 'date', 'company_sell', 'company_buy', 'price')
    list_filter = ('date', 'company_sell', 'company_buy')
    search_fields = ('company_sell', 'company_buy')

@admin.register(Wire)
class WireAdmin(admin.ModelAdmin):
    list_display = ('count', 'date', 'company_sell', 'company_buy', 'price')
    list_filter = ('date', 'company_sell', 'company_buy')
    search_fields = ('company_sell', 'company_buy')

@admin.register(Armature)
class ArmatureAdmin(admin.ModelAdmin):
    list_display = ('count', 'date', 'company_sell', 'company_buy', 'price')
    list_filter = ('date', 'company_sell', 'company_buy')
    search_fields = ('company_sell', 'company_buy')

@admin.register(Brigade)
class BrigadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
@admin.register(WirehouseB)
class BrigadeAdmin(admin.ModelAdmin):
    list_display = ('id', )

@admin.register(WirehouseV)
class BrigadeAdmin(admin.ModelAdmin):
    list_display = ('id', )

@admin.register(BrigadeWork)
class BrigadeWorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(NamePile)
class NamePileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'pile_type')
    list_filter = ('pile_type',)
    search_fields = ('name',)


@admin.register(Pile)
class PileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'size', 'count', 'defect')
    list_filter = ('name',)
    search_fields = ('name__name', 'size')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'role')
    list_filter = ('role',)
    search_fields = ('user__username', 'role__name')

@admin.register(Car)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('model', 'number','weight')

@admin.register(OperationArrival)
class OperationArrivalAdmin(admin.ModelAdmin):
    list_display = ('id',  'date')




@admin.register(OperationDeparture)
class OperationDepartureAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'confirm', 'number_car', 'brigade')



@admin.register(ReturnPile)
class ReturnPileAdmin(admin.ModelAdmin):
    list_display = ('id', 'pile', 'quantity', 'date')
    list_filter = ('date',)
    search_fields = ('pile__name__name',)
    filter_horizontal = ('user',)

@admin.register(Order)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('piles_info',)


admin.site.register(Tube)
admin.site.register(Lists)
admin.site.register(Lopasti)
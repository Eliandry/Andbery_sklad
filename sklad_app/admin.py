from django.contrib import admin

from .models import *

admin.site.register(Wire4)
admin.site.register(Wire6)
@admin.register(Beton)
class BetonAdmin(admin.ModelAdmin):
    list_display = ('count', 'date', 'company_sell', 'company_buy', 'price')
    list_filter = ('date', 'company_sell', 'company_buy')
    search_fields = ('company_sell', 'company_buy')

class BrigadeAdmin(admin.ModelAdmin):
    list_display = ('id', )
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
@admin.register(Armature10)
class Armature10Admin(admin.ModelAdmin):
    list_display = ('count', 'date', 'company_sell', 'company_buy', 'price')
    list_filter = ('date', 'company_sell', 'company_buy')
    search_fields = ('company_sell', 'company_buy')
@admin.register(Brigade)
class BrigadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


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


@admin.register(WirehouseB)
class BrigadeAdmin(admin.ModelAdmin):
    list_display = ('id', )

@admin.register(OperationDeparture)
class OperationDepartureAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'confirm', 'number_car', 'brigade')


@admin.register(Order)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('date',)

@admin.register(ReturnPile)
class ReturnPileAdmin(admin.ModelAdmin):
    list_display = ('id', 'pile', 'quantity', 'date')
    list_filter = ('date',)
    search_fields = ('pile__name__name',)
    filter_horizontal = ('user',)

admin.site.register(SendOperation)
admin.site.register(SendDetail)
admin.site.register(ReturnPiles)
admin.site.register(UserBrigade)
admin.site.register(OperationDepCount)
admin.site.register(Debt)
admin.site.register(Del_mat)
admin.site.register(Order_v)
admin.site.register(OperationArrival_V)
admin.site.register(Tube)
admin.site.register(Tube108)
admin.site.register(Tube108_2)
admin.site.register(Tube133)
admin.site.register(Lists)
admin.site.register(Lists5)
admin.site.register(Lopasti)
admin.site.register(MBP)
admin.site.register(MBP_stat)
@admin.register(WirehouseV)
class BrigadeAdmin(admin.ModelAdmin):
    list_display = ('id', )

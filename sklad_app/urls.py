from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from .views import *
urlpatterns = [
    path('operation/arrival/', operation_arrival_view, name='operation_arrival'),
    path('operation/departure/', operation_departure_view, name='operation_departure'),
    path('',main,name='main'),
    path('ajax/load-piles/', load_piles, name='ajax_load_piles'),
    path('warehouse-statistics/', warehouse_statistics, name='warehouse_statistics'),
    path('return_piles/',return_pile_view,name='return_pile'),
    path('add-pile/', add_pile, name='add_pile'),
    path('ajax/load-brigades/', load_brigades, name='ajax_load_brigades'),
    path('confirm_operations/', confirm_operations, name='confirm_operations'),
    path('confirm-return-pile/', confirm_return_pile, name='confirm_return_pile'),
    path('search_departures/', search_departures, name='search_departures'),
    path('get-car-numbers/', get_car_numbers, name='get-car-numbers'),
    path('operation/departure/ajax/load/pile/weight/', load_pile_weight, name='ajax_load_piles_weight'),
    path('operation/departure/ajax/load/car/weight/', load_car_weight, name='ajax_load_cars_weight'),
    path('add_beton/', add_beton, name='add_beton'),
    path('add_wire/', add_wire, name='add_wire'),
    path('add_armature/', add_armature, name='add_armature'),
    path('search/', search_by_date_range, name='search'),
]
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from .views import *
urlpatterns = [
    #ЖБ
    path('operation/arrival/', operation_arrival_view, name='operation_arrival'),
    path('operation/departure/', operation_departure_view, name='operation_departure'),
    path('add_beton/', add_beton, name='add_beton'),
    path('add_wire/', add_wire, name='add_wire'),
    path('add_wire4/', add_wire4, name='add_wire4'),
    path('add_wire6/', add_wire6, name='add_wire6'),
    path('add_armature/', add_armature, name='add_armature'),
    path('add_armature10/', add_armature10, name='add_armature10'),
    path('warehouse-statistics/', warehouse_statistics, name='warehouse_statistics'),
    path('jb/',jb,name='jb'),
    path('prod-class/',classif,name='classes'),
    path('order/',create_order,name='order'),
    path('process_text_view/', process_text_view, name='process_text_view'),
    path('add-pile/', add_pile, name='add_pile'),
    path('debts/', DebtListView.as_view(), name='debt_list'),
    path('debts/<int:brigade_id>/', DebtDetailView.as_view(), name='debt_detail'),
    path('update_send_operation/<int:operation_id>/', update_send_operation, name='update_send_operation'),
    path('add_pile_to_count/<int:count_id>/', add_pile_to_count, name='add_pile_to_count'),

    #Винты
    path('warehouseV_statistics/', warehouseV_statistics, name='warehouseV_statistics'),
    path('prodV-class/',classifV,name='classesV'),
    path('add_lists/', add_lists, name='add_lists'),
    path('add_tube/', add_tube, name='add_tube'),
    path('add_tube108/', add_tube108, name='add_tube108'),
    path('add_tube108_2/', add_tube108_2, name='add_tube108_2'),
    path('add_tube133/', add_tube133, name='add_tube133'),
    path('calc_lop/', calculate_lopasti, name='calc_lop'),
    path('materialsV_overview/',materialsV_overview,name='materialsV_overview'),
    path('vint/',vint,name='vint'),
    path('cut_tube/',calculate_tube_cutting,name='cut_tube'),

    #Подтверждения
    path('confirm_operations/', confirm_operations, name='confirm_operations'),
    path('confirm_operation/', confirm_operation_view, name='confirm_operation'),
    path('confirm_departures/', confirm_departures_view, name='confirm_departures'),
    path('confirm_sklad_list/', ConfirmSkladView.as_view(), name='confirm_sklad_list'),



    #Статистика и excel
    path('mbp_statistics/',mbp_statistics,name='mbp_statistics'),
    path('search/', search_by_date_range, name='search'),
    path('materials_overview/', materials_overview, name='materials_overview'),
    path('mat/', mat, name='mat'),
    path('export_dep/', export_operation_departures_to_excel, name='export_dep'),
    path('export/operation_arrivals/', export_operation_arrivals_to_excel, name='export_operation_arrivals_to_excel'),
    path('download-orders/', download_orders, name='download_orders'),
    path('export-material/', export_material_data, name='export_material_data'),
    path('stat_mbp/', display_mbp_stats, name='stat_mbp'),
    path('display_debts/', display_debts, name='display_debts'),
    path('excel/', download_excel, name='excel'),
    path('operation_arrival_list/', operation_arrival_list, name='operation_arrival_list'),
    path('return_piles_list/', ReturnPilesListView.as_view(), name='return_piles_list'),




    path('', main, name='main'),









    path('orders_by_day/',orders_by_day,name='orders_by_day'),
    path('ware/',ware,name='ware'),
    path('update_mbp/',update_mbp_view,name='update_mbp'),
    path('add_mbp/',add_mbp_view,name='add_mbp'),
    path('order_tube_cutting/',order_tube_cutting,name='order_tube_cutting'),
    path('latest_deliveries/', latest_deliveries, name='latest_deliveries'),
    path('add_debt/', AddDebtView.as_view(), name='add_debt'),
    path('update-pile-count/<int:count_id>/', update_pile_count, name='update_pile_count'),
    path('operation-dep-count/', list_operation_dep_count, name='list_operation_dep_count'),
    path('return_piles/', ReturnPilesView.as_view(), name='return_piles'),



]
from . import views
from django.urls import path, include

app_name='management'

urlpatterns = [

    path('adjustment_reprocess/', views.adjustment_reprocess , name = 'adjustment_reprocess'),
    path('asrsusageReport/', views.asrsusageReport , name = 'asrsusageReport'),
    path('changepassword/', views.changepassword , name = 'changepassword'),
    path('company/', views.company , name = 'company'),
    path('detailreport/', views.detailreport , name = 'detailreport'),
    path('employee/', views.employee , name = 'employee'),
    path('header/', views.header , name = 'header'),
    path('material_inword', views.material_inword , name = 'material_inword'),
    path('material_outword', views.material_outword , name = 'material_outword'),
    path('material_reload', views.material_reload , name = 'material_reload'),
    path('pallet_q', views.pallet_q , name = 'pallet_q'),
    path('pallet', views.pallet , name = 'pallet'),
    path('q_status', views.q_status , name = 'q_status'),
    path('screen_storage', views.screen_storage , name = 'screen_storage'),
    path('shifts', views.shifts , name = 'shifts'),
    path('summaryreport', views.summaryreport , name = 'summaryreport'),

]
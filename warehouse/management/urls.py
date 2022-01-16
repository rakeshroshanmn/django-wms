from . import views as user_views
from django.urls import path, include

app_name='management'

urlpatterns = [

    path('', user_views.signin , name = 'signin'),
    path('adjustment_reprocess/', user_views.adjustment_reprocess , name = 'adjustment_reprocess'),
    path('asrsusageReport/', user_views.asrsusageReport , name = 'asrsusageReport'),
    path('changepassword/', user_views.changepassword , name = 'changepassword'),
    path('company/', user_views.company , name = 'company'),
    path('detailreport/', user_views.detailreport , name = 'detailreport'),
    path('employee/', user_views.employee , name = 'employee'),
    path('header/', user_views.header , name = 'header'),
    path('material_inword', user_views.material_inword , name = 'material_inword'),
    path('material_outword', user_views.material_outword , name = 'material_outword'),
    path('material_reload', user_views.material_reload , name = 'material_reload'),
    path('pallet_q', user_views.pallet_q , name = 'pallet_q'),
    path('pallet', user_views.pallet , name = 'pallet'),
    path('q_status', user_views.q_status , name = 'q_status'),
    path('screen_storage', user_views.screen_storage , name = 'screen_storage'),
    path('shifts', user_views.shifts , name = 'shifts'),
    path('summaryreport', user_views.summaryreport , name = 'summaryreport'),

]
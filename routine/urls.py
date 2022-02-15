from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.homepage, name='homepage'),
    path('computer_batch', views.computerBatch, name='computer_batch'),
    path('electrical_batch', views.electricalBatch, name='electrical_batch'),
    path('addComputer_first', views.computerData_first, name='addComputerfirst'),
    path('addComputer_second', views.computerData_second, name='addComputersecond'),
    path('addComputer_third', views.computerData_third, name='addComputerthird'),
    path('addComputer_fourth', views.computerData_fourth, name='addComputerfourth'),
    path('addElectrical_first', views.electricalData_first, name='addElectricalfirst'),
    path('addElectrical_second', views.electricalData_second, name='addElectricalsecond'),
    path('addElectrical_third', views.electricalData_third, name='addElectricalthird'),
    path('addElectrical_fourth', views.electricalData_fourth, name='addElectricalfourth'),
    path('generate_routine', views.generate_routine, name='generate_routine'),
    path('teacher_code', views.generate_code, name='teacher_code'),
    
]

from django.urls import path
from nucleo import views

app_name = "nucleo"

urlpatterns = [
    
    path('home', views.home, name= "home"),

    path('medicamento/', views.medicamento, name="indexMedicamento"),
    path('medicamento/create/', views.medicamentoCreate.as_view(), name="crearMedicamento"),
    path('medicamento/update/<int:pk>/', views.medicamentoUpdate.as_view(), name="actualizarMedicamento"),
    path('medicamento/delete/<int:pk>/', views.medicamentoDelete, name="eliminarMedicamento"),

    path('especialidad/', views.medicosEspecilidad.as_view(), name="especialidad"),
]
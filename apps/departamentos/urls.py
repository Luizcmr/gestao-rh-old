from django.urls import path
from .views import DepartamentoCreate, DepartamentoEdit, DepartamentoList, DepartamentoDelete


urlpatterns = [
    path('departamento', DepartamentoList.as_view(), name="lista_departamentos"),
    path('novo', DepartamentoCreate.as_view(), name='create_departamento'),
    path('editar/<int:pk>/', DepartamentoEdit.as_view(), name='edit_departamento'),
    path('excluir/<int:pk>', DepartamentoDelete.as_view(), name="deleta_departamento"),
]
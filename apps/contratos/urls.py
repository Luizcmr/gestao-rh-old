from django.urls import path
from . import views
from .views import ContratoCreate, ContratoEdit, ContratoList, ContratoDelete

urlpatterns = [
    path('Contrato', ContratoList.as_view(), name="lista_contratos"),
    path('novo', ContratoCreate.as_view(), name='create_contrato'),
    path('editar/<int:pk>/', ContratoEdit.as_view(), name='edit_contrato'),
    path('excluir/<int:pk>', ContratoDelete.as_view(), name="deleta_contrato"),
    path('ajax/load-funcionarios/', views.load_funcionarios, name='ajax_load_funcionarios'),  # <-- this one here
]
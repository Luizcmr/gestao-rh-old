from django.urls import path
from .views import ContratoCreate, ContratoEdit, ContratoList, ContratoDelete

urlpatterns = [
    path('Contrato', ContratoList.as_view(), name="lista_contratos"),
    path('novo', ContratoCreate.as_view(), name='create_contrato'),
    path('editar/<int:pk>/', ContratoEdit.as_view(), name='edit_contrato'),
    path('excluir/<int:pk>', ContratoDelete.as_view(), name="deleta_contrato"),

]
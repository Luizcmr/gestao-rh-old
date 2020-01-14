from django.urls import path
from .views import BeneficioCreate, BeneficioEdit, BeneficioList, BeneficioDelete

urlpatterns = [
    path('Beneficio', BeneficioList.as_view(), name="lista_beneficios"),
    path('novo', BeneficioCreate.as_view(), name='create_beneficio'),
    path('editar/<int:pk>/', BeneficioEdit.as_view(), name='edit_beneficio'),
    path('excluir/<int:pk>', BeneficioDelete.as_view(), name="deleta_beneficio"),
]
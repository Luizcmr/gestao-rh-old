from django.urls import path
from .views import Beneficios_funcCreate, Beneficios_funcDelete

urlpatterns = [
    #path('documento', Dependentes_funcList.as_view(), name="lista_documentos"),
    path('novo/<int:contrato_id>/',Beneficios_funcCreate.as_view(), name='create_beneficios_func'),
    #path('editar/<int:pk>/', Dependentes_funcEdit.as_view(), name='edit_documento'),
    path('excluir/<int:pk>', Beneficios_funcDelete.as_view(), name="deleta_beneficios_func"),
]
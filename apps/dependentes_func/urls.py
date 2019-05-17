from django.urls import path
from .views import Dependentes_funcCreate, Dependentes_funcDelete

urlpatterns = [
    #path('documento', Dependentes_funcList.as_view(), name="lista_documentos"),
    path('novo/<int:funcionario_id>/',Dependentes_funcCreate.as_view(), name='create_dependentes_func'),
    #path('editar/<int:pk>/', Dependentes_funcEdit.as_view(), name='edit_documento'),
    path('excluir/<int:pk>', Dependentes_funcDelete.as_view(), name="deleta_dependentes_func"),
]
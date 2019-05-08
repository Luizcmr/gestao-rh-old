from django.urls import path
from .views import FuncaoCreate, FuncaoEdit, FuncaoList, FuncaoDelete

urlpatterns = [
    path('funcao', FuncaoList.as_view(), name="lista_funcoes"),
    path('novo', FuncaoCreate.as_view(), name='create_funcao'),
    path('editar/<int:pk>/', FuncaoEdit.as_view(), name='edit_funcao'),
    path('excluir/<int:pk>', FuncaoDelete.as_view(), name="deleta_funcao"),
]
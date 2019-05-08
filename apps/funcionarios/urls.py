from django.urls import path
from .views import FuncionarioCreate, FuncionarioEdit, FuncionarioList, FuncionarioDelete

urlpatterns = [
    path('funcionario', FuncionarioList.as_view(), name="lista_funcionarios"),
    path('novo', FuncionarioCreate.as_view(), name='create_funcionario'),
    path('editar/<int:pk>/', FuncionarioEdit.as_view(), name='edit_funcionario'),
    path('excluir/<int:pk>', FuncionarioDelete.as_view(), name="deleta_funcionario"),

]
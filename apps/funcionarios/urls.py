from django.urls import path
from .views import FuncionarioCreate, FuncionarioEdit, FuncionarioList, FuncionarioDelete, FuncionarioTransfere
#from .views import funcionarios_update

urlpatterns = [
    path('funcionario', FuncionarioList.as_view(), name="lista_funcionarios"),
    path('novo', FuncionarioCreate.as_view(), name='create_funcionario'),
    path('editar/<int:pk>/', FuncionarioEdit.as_view(), name='edit_funcionario'),
    path('excluir/<int:pk>', FuncionarioDelete.as_view(), name="deleta_funcionario"),
    path('transferir/<int:pk>/', FuncionarioTransfere.as_view(), name="transfere_funcionario"),

]
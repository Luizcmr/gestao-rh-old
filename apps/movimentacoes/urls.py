from django.urls import path
from . import views
from .views import MovimentacaoCreate, MovimentacaoEdit, MovimentacaoList, MovimentacaoDelete

urlpatterns = [
    path('Movimentacao', MovimentacaoList.as_view(), name="lista_movimentacoes"),
    path('novo', MovimentacaoCreate.as_view(), name='create_movimentacao'),
    path('editar/<int:pk>/', MovimentacaoEdit.as_view(), name='edit_movimentacao'),
    path('excluir/<int:pk>', MovimentacaoDelete.as_view(), name="deleta_movimentacao"),
 ]
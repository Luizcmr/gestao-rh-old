from django.urls import path
from . import views
from .views import MovimentacaoCreate, MovimentacaoEdit, MovimentacaoList, MovimentacaoDelete
from .views import EventosAVencerExcel, EventosAVencerPDF, EventosAVencer

urlpatterns = [
    path('Movimentacao', MovimentacaoList.as_view(), name="lista_movimentacoes"),
    path('novo', MovimentacaoCreate.as_view(), name='create_movimentacao'),
    path('editar/<int:pk>/', MovimentacaoEdit.as_view(), name='edit_movimentacao'),
    path('excluir/<int:pk>', MovimentacaoDelete.as_view(), name="deleta_movimentacao"),
    path('eventos-a-vencer', EventosAVencer.as_view(), name="eventos_a_vencer"),
    path('exportar-excel', EventosAVencerExcel.as_view(), name='eventos-a-vencer-excel'),
    path('exportar-pdf', EventosAVencerPDF.as_view(), name='eventos-a-vencer-pdf'),
 ]
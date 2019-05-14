from django.urls import path
from .views import EventoCreate, EventoEdit, EventoList, EventoDelete

urlpatterns = [
    path('evento', EventoList.as_view(), name="lista_eventos"),
    path('novo', EventoCreate.as_view(), name='create_evento'),
    path('editar/<int:pk>/', EventoEdit.as_view(), name='edit_evento'),
    path('excluir/<int:pk>', EventoDelete.as_view(), name="deleta_evento"),
]
from django.urls import path
from .views import HorarioCreate, HorarioEdit, HorarioList, HorarioDelete

urlpatterns = [
    path('Horario', HorarioList.as_view(), name="lista_horarios"),
    path('novo', HorarioCreate.as_view(), name='create_horario'),
    path('editar/<int:pk>/', HorarioEdit.as_view(), name='edit_horario'),
    path('excluir/<int:pk>', HorarioDelete.as_view(), name="deleta_horario"),
]
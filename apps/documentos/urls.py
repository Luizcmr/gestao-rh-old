from django.urls import path
from .views import DocumentoCreate

urlpatterns = [
    #path('documento', DocumentoList.as_view(), name="lista_documentos"),
    path('novo/<int:funcionario_id>/', DocumentoCreate.as_view(), name='create_documento'),
    #path('editar/<int:pk>/', DocumentoEdit.as_view(), name='edit_documento'),
    #path('excluir/<int:pk>', DocumentoDelete.as_view(), name="deleta_documento"),
]
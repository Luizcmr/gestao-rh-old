from django.urls import path
from .views import EmpresaCreate, EmpresaEdit, EmpresaList, EmpresaDelete

urlpatterns = [
    path('novo', EmpresaCreate.as_view(), name='create_empresa'),
    path('editar/<int:pk>/', EmpresaEdit.as_view(), name='edit_empresa'),
    path('empresa', EmpresaList.as_view(), name="lista_empresas"),
    path('excluir/<int:pk>', EmpresaDelete.as_view(), name="deleta_empresa"),

]
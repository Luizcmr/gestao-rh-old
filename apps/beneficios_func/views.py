from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView,DeleteView
from django.urls import reverse_lazy

from .models import Beneficios_func

class Beneficios_funcCreate(CreateView):
    model = Beneficios_func
    fields = ['beneficio','valor', 'status']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.contrato_id = self.kwargs['contrato_id']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return HttpResponse("Erro na entrada de dados dos Campos")


class Beneficios_funcDelete(DeleteView):
    model = Beneficios_func
    #success_url = reverse_lazy('edit_funcionario', args=[Documento.funcionario])

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = reverse_lazy('edit_contrato', kwargs={'pk': self.object.contrato_id})
        self.object.delete()

        return HttpResponseRedirect(success_url)
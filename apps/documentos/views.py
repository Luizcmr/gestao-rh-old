from django.http import HttpResponseRedirect
from django.views.generic import CreateView,DeleteView
from django.urls import reverse_lazy

from .models import Documento

class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.funcionario_id = self.kwargs['funcionario_id']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class DocumentoDelete(DeleteView):
    model = Documento
    #success_url = reverse_lazy('edit_funcionario', args=[Documento.funcionario])

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = reverse_lazy('edit_funcionario', kwargs={'pk': self.object.funcionario_id})
        self.object.delete()

        return HttpResponseRedirect(success_url)
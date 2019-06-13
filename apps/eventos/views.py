from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Evento


class EventoCreate(CreateView):
    model = Evento
    fields = ['nome']

    def form_valid(self, form):
        obj = form.save()
        return redirect('lista_eventos')

class EventoEdit(UpdateView):
    model = Evento
    fields = ['id','nome']

class EventoList(ListView):
    model = Evento
    fields = ['nome']

class EventoDelete(DeleteView):
    model = Evento
    success_url = reverse_lazy("lista_eventos")
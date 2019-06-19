from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Evento


class EventoCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'eventos.add_evento'
    model = Evento
    fields = ['id','nome']

    def form_valid(self, form):
        obj = form.save()
        return redirect('lista_eventos')

class EventoEdit(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'eventos.edit_evento'
    model = Evento
    fields = ['id','nome']

class EventoList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'eventos.view_evento'
    model = Evento
    fields = ['id','nome']

class EventoDelete(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'eventos.delete_evento'
    model = Evento
    success_url = reverse_lazy("lista_eventos")
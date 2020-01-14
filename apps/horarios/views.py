from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Horario


class HorarioCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'horarios.add_horario'
    model = Horario
    fields = ['descricao','hora_entrada', 'hora_saida','intervalo_entrada','intervalo_saida']

    def form_valid(self, form):
        obj = form.save()
        return redirect('lista_horarios')


class HorarioEdit(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'horarios.change_horario'
    model = Horario
    fields = ['descricao','hora_entrada', 'hora_saida','intervalo_entrada','intervalo_saida']

class HorarioList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'horarios.view_Horario'
    model = Horario
    fields = ['descricao','hora_entrada', 'hora_saida','intervalo_entrada','intervalo_saida']

class HorarioDelete(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'horarios.delete_Horario'
    model = Horario
    success_url = reverse_lazy("lista_horarios")
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Beneficio


class BeneficioCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'beneficios.add_beneficio'
    model = Beneficio
    fields = ['nome']

    def form_valid(self, form):
        obj = form.save()
        return redirect('lista_beneficios')


class BeneficioEdit(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'beneficios.change_beneficio'
    model = Beneficio
    fields = ['nome']

class BeneficioList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'beneficios.view_beneficio'
    model = Beneficio
    fields = ['nome']

class BeneficioDelete(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'beneficios.delete_beneficio'
    model = Beneficio
    success_url = reverse_lazy("lista_beneficios")
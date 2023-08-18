from django.shortcuts import render
from django.contrib.auth.views import LoginView

class loginforview(LoginView):
    template_name ="login.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']="Iniciar sesion"
        return context
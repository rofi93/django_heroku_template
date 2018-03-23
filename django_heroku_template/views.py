from django.views.generic.base import View
from django.shortcuts import render


class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        template_name = 'home.html'
        return render(request, template_name, context)

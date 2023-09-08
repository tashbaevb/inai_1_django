from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView, FormView
from . import parser, models, forms


class ParserView(ListView):
    model = models.Clothes
    template_name = 'clothes_list.html'
    context_object_name = 'suka'

    def get_queryset(self):
        return models.Clothes.objects.all()


class ParserFormView(FormView):
    template_name = 'parser_clothes.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('<h1>Ready!!!</h1>')
        else:
            return super(ParserFormView, self).post(request, *args, **kwargs)





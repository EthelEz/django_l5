from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                    CreateView, UpdateView, DeleteView)
from . import models

# from django.http import HttpResponse

# Describes how to create your views function view.
# def index(request):
#     return render(request, 'cvb_app/index.html')

#Describes how to create class based view
# class CBView(View):
#     def get(self, request):
#         return HttpResponse('CLASS BASED VIEW ARE COOL')

#Describes how to create template view
class IndexView(TemplateView):
    template_name = 'index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['injectme'] = 'BASIC INJECTION'
#         return context

#Describes the creation of list view
# NB: These are the two ost generic views you'd see in peoples projects
class SchoolListView(ListView):
    # context_object_name ='schools'
    model = models.School
# the context_object_name returns the list of schools inside the model School

#Describes the creation of Detail view
class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'cbv_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location', 'num_students')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal', 'num_students')
    model = models.School

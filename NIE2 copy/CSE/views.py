from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def products(request):
    return render(request,'products.html')

def service(request):
    return render(request,'service.html')

def contacts(request):
    return render(request,'contacts.html')


def basic(request):
    return render(request,'basic.html')
def studentList(request):
    return render(request,'studentList.html')

from CSE.models import Student
def studentList(request):
    students = Student.objects.all()
    context = {'students':students}
    return render(request,'studentList.html', context)
from CSE.models import Student
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

class StuList(ListView):
    model = Student
    template_name = 'CBV/list.html'


class Forms(CreateView):
    model = Student
    fields = '__all__'
    template_name = 'CBV/forms.html'
    success_url = '/'


class StudentDetail(DetailView):
    model = Student
    template_name = 'CBV/detail.html'

class StudentUpdate(UpdateView):
    model = Student
    fields = '__all__'
    template_name = 'CBV/update.html'
    success_url = '/'

class StudentDelete(UpdateView):
    model = Student
    fields = '__all__'
    template_name = 'CBV/delete.html'
    success_url = '/'
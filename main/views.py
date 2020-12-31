from django.shortcuts import render, redirect
from django.views.generic import DetailView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
# Create your views here.
def index(request):
    return render(request, 'mainpage.html')

class listTodo(LoginRequiredMixin,ListView):
    model = Todo
    template_name = 'todo_list.html'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["object_list"] = Todo.objects.filter(todo_user=self.request.user)
            return context
        

class createTodo(LoginRequiredMixin,CreateView):
    model = Todo
    fields = ['title','description','date']
    template_name = 'todo_create.html'
    success_url = reverse_lazy('todo-list')

    def get_form(self):
        form = super(createTodo, self).get_form()
        form.fields['date'].widget = widgets.DateInput(attrs={'type': 'date'})

        return form
    
    def form_valid(self, form):
        form.instance.todo_user = self.request.user
        return super().form_valid(form)

class detailTodo(LoginRequiredMixin,DetailView):
    model = Todo
    template_name = "todo_detail.html"

    def get_context_data(self, **kwargs):
        context = super(detailTodo, self).get_context_data(**kwargs)
        return context

class updateTodo(LoginRequiredMixin,UpdateView):
    model = Todo
    fields = ['title','description','date']
    template_name = 'todo_create.html'
    success_url = reverse_lazy('todo-list')

    def get_form(self):
        form = super(updateTodo, self).get_form()
        form.fields['date'].widget = widgets.DateInput(attrs={'type': 'date'})

        return form
    
    def form_valid(self, form):
        form.instance.todo_user = self.request.user
        return super().form_valid(form)

@login_required
def completed(request, pk):

    todo = Todo.objects.filter(pk = pk).update(completed= True)
    # todo.completed = True
    # todo.save(update_fields=['completed'])
    print(todo)

    return redirect('todo-list')

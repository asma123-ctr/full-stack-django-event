from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from cms.ajax_views import (AjaxDetailView, AjaxCreateView , AjaxUpdateView, AjaxDeleteView)
from cms.mixins import ModelMixin
from .models import Todo
from .forms import TodoForm,NewUserForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.shortcuts import  render, redirect
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



class TodoList(LoginRequiredMixin,ModelMixin, ListView):
    ajax_partial = 'todo/partials/todo_list_partial.html'
   
    #obj=Todo.objects.filter(name="tesdt")
    model = Todo
    def get_queryset(self):
    	
    	return Todo.objects.filter(user_id=self.request.user.id)


class TodoDetail(LoginRequiredMixin,AjaxDetailView, ModelMixin, DetailView):
    ajax_partial = 'todo/partials/todo_detail_partial.html'
    model = Todo
    

class TodoCreate(LoginRequiredMixin,AjaxCreateView,ModelMixin, CreateView):
    model = Todo
    form_class = TodoForm
    ajax_partial = 'todo/partials/todo_form_partial.html'
    ajax_list_partial = 'todo/partials/todo_list_partial.html'
    def get_queryset(self):
    	
    	return Todo.objects.filter(user_id=self.request.user.id)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TodoUpdate(LoginRequiredMixin,AjaxUpdateView,ModelMixin, UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo/todo_form.html'
    ajax_partial = 'todo/partials/todo_form_partial.html'
    ajax_list_partial = 'todo/partials/todo_list_partial.html'
    def get_queryset(self):
    	
    	return Todo.objects.filter(user_id=self.request.user.id)


class TodoDelete(LoginRequiredMixin,AjaxDeleteView, ModelMixin, DeleteView):
    model = Todo
    ajax_partial = 'todo/partials/todo_delete_partial.html'
    ajax_list_partial = 'todo/partials/todo_list_partial.html'
    success_url = reverse_lazy('todo:todo-list')
    def get_queryset(self):
    	
    	return Todo.objects.filter(user_id=self.request.user.id)


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("todo:todo-list")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="todo/login.html", context={"login_form":form})

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("todo:todo-list")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request=request, template_name="todo/register.html", context={"register_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("todo:login")
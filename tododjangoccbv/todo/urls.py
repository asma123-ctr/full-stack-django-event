from django.urls import path

from .views import TodoList, TodoDetail, TodoCreate, TodoUpdate, TodoDelete,register_request,login_request,logout_request


app_name = 'todo'
urlpatterns = [
    path('', TodoList.as_view(), name='todo-list'),
    path('<int:pk>/', TodoDetail.as_view(), name='todo-detail'),
    path('create/', TodoCreate.as_view(), name='todo-create'),
    path('update/<int:pk>/', TodoUpdate.as_view(), name='todo-update'),
    path('delete/<int:pk>/', TodoDelete.as_view(), name='todo-delete'),
    path("register", register_request, name="register"),
    path("login", login_request, name="login"),
    path("logout", logout_request, name= "logout"),

]

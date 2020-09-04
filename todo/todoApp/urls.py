from django.urls import path
from django.contrib import admin

from . import views
from django.conf.urls import url
urlpatterns = [
    url(r"^admin",admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^add_todo/',views.add_todo,name='addtodo'),
    path('done_task/<int:task_id>',views.done_task,name="done_task"),
    path('login_request/',views.login_request,name="login"),
    path('Register/',views.register,name="register"),
    path('register/login_request/',views.login_request,name="login"),
    path('logout_request/', views.logout_request, name="logout"),
]
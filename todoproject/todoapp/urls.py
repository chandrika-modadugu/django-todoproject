from django.urls import path
from todoapp import views

app_name='todoapp'
urlpatterns = [
path('home/',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('AddTask/<str:username>/',views.AddTask,name='AddTask'),
    path('ViewTask/<str:username>/',views.ViewTask,name='ViewTask'),
    path('edittask/<str:username>/<str:Title>/',views.edittask,name='edittask'),
    path('deletetask/<str:username>/<str:Title>/',views.deletetask,name='deletetask'),
]

from django.urls import path

from studentapp import views

urlpatterns = [
    path('', views.log_fun, name='log'),
    path('logdata', views.logdata_fun),
    path('reg', views.reg_fun, name='reg'),
    path('regdata', views.regdata_fun),
    path('home', views.home,name='home'),
    path('add_students', views.addstudent_fun,name='add'),
    path('readdata', views.readdata_fun),
    path('display',views.display_fun,name='display'),
    path('update/<int:id>',views.update_fun,name='up'),
    path('delete/<int:id>',views.delete_fun,name='del'),
    path('log_out',views.log_out_fun,name='log_out')
]
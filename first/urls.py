
from django.contrib import admin
from django.urls import path
from first import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('loginportal/', views.admin_login),
    path('about-us/', views.yash),
    # path('course/<values>',views.course),
    path('login/', views.form),
    path('/submitform/', views.submit)

]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('print_data/', views.print_data, name='print_data'),
    path('check_by_id/<int:id>', views.details, name='details'),
]

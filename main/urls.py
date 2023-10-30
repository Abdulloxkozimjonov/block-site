from django.urls import path
from .views import *

urlpatterns = [
    path('',login_view,name="login_url"),
    path('log-out/',log_out_view,name="log_out_url"),
    path('edit/<int:pk>/',edit_user_view,name="update_url"),
    path('register/', register_view, name="register_url"),
    path('index/',index_view,name="index_url"),
    path('about/', about_view, name="about_url"),
    path('courses/', courses_view, name="courses_url"),
    path('price/', price_view, name="price_url"),
    path('create-contact/', create_contact_view, name="create_contact_url"),
    path('videos/', videos_view, name="videos_url"),
    path('contact/', contact_view, name="contact_url"),
    path('my-profile/<int:pk>/', my_profile_view, name="my_profile_url")
]
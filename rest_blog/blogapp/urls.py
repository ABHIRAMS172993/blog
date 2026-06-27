
from .views import create_blog,view_blog,edit_blog,delete_blog,user_login,register_login,view_blog_user
from django.urls import path
urlpatterns = [
   path('',view_blog),
   path('create/',create_blog),
   path('edit/<int:id>/',edit_blog),
   path('delete/<int:id>/',delete_blog),
]
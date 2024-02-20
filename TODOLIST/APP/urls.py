
from django.urls import path
from .views import list,detail,create,update,delete,login,register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', list.as_view(),name='list'),
    path('list/<int:pk>/', detail.as_view(),name='detial'),
    path('create/',create.as_view(),name='create'),
    path('update/<int:pk>',update.as_view(),name='update'),
    path('delete/i<int:pk>',delete.as_view(),name='delete'),
    path('login/',login.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('signin/',register.as_view(),name='signin')
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('<int:pk>/bookdetails/', views.BookDetailsView.as_view(), name='book_details'),
    path('bookcreate/', views.BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/bookupdate/', views.BookUpdateView.as_view(), name='book_update'),
]

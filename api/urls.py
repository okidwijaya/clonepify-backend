from django.urls import path
from . import views

urlpatterns = [
    path("notes/", views.NoteListCreate.as_view(), name="note-list"),
    path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note"),
    path('products/', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', views.ProductListRetrieveUpdateView.as_view(), name='product-detail'),
    path('images/<str:image_name>/', views.serve_image, name='serve_image'),
    path('blogpost/', views.BlogpostListCreateView.as_view(), name='blogpost-list-create'),
    path('blogpost/<int:pk>/', views.BLogpostListRetrieveUpdateView.as_view(), name='blogpost-detail'),
]

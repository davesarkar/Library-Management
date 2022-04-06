from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.getRoutes),
    path('register/', views.register),
    path('view-books/', views.viewBooks),
    path('add-book/', views.addBook),
    path('view-book/<str:id>/', views.viewBook),
    path('edit-book/<str:id>/', views.editBook),
    path('delete-book/<str:id>/', views.deleteBook),
    
    path('/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

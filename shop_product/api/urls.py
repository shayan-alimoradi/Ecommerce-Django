from django.urls import path
from . import views

app_name = 'api-comment'


urlpatterns = [
    path('list/', views.CommentListView.as_view(), name='comment-list'),
    path('<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail'),
]
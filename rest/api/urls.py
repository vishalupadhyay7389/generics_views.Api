from django.urls import path
from api.views import StudentDetailView , StudentDeatilListView

urlpatterns = [
    path('api/', StudentDetailView.as_view() , name='student'),
    path('api/<int:pk>/', StudentDeatilListView.as_view() , name='students'),
]
from django.urls import path
from .views import StartView, InputNumberView


urlpatterns = [
    path('', StartView.as_view(), name='user_num'),
    path('user_choice/', InputNumberView.as_view(), name='write_num'),
]

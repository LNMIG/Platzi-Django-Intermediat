from django.urls import path
from . import views
from . import views_class


app_name = 'apps.polls'

urlpatterns = [
    path('', views_class.IndexView.as_view(), name='index'),
    path('detail/<int:pk>', views_class.DetailView.as_view(), name='detail'),
    path('result/<int:pk>', views_class.ResultView.as_view(), name='result'),
    path('vote/<int:question_id>', views.vote, name='vote'),
]
from django.urls import path
from .views import home,forecast

app_name='weather'

urlpatterns = [
    path('',home,name='home_page'),
    path('forecast/',forecast,name='forecast_page')
]

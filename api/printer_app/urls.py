from django.urls import path
from printer_app.views import checks


urlpatterns = [
    path('', checks),
]

from . import views
from django.urls import path
urlpatterns = [
    path('', view=views.translator_view, name='translator_view')
]

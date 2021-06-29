from django.urls import path

from .views import *

urlpatterns = [
    path('aeroportos/<cidade>/<estado>', AeroportoDados.as_view()),
    path('voos/<id>', VooDados.as_view()),

]

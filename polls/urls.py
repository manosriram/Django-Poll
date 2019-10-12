from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:qID>', views.detail, name="detail"),
    path('<int:qID>/results', views.results, name="results"),
    path('<int:qID>/vote', views.vote, name="vote")
]

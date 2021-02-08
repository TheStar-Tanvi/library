from django.urls import path
from .views import issue,home

urlpatterns = [

    path('issue',issue,name="issue"),
    path("",home,name = 'home')

]
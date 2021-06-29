
from django.urls import path

from .views import index, Addetails, searchinput, find, update, delete

urlpatterns = [
    path('', index, name='index'),
    path('Addetails/', Addetails, name='Addetails'),
    path('searchinput/', searchinput, name='searchinput'),
    path('find/', find, name='find'),
    path('update/', update, name='update'),
    path('delete/', delete, name='delele'),

]

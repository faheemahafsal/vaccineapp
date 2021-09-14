from django.urls import path
from . import views

urlpatterns=[
    path('',views.task_view,name='result'),
    path('delete/<int:registrationid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
]
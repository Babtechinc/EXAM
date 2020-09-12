from django.urls import path
from examportal import views

urlpatterns = [
    path('i',views.api , name='api'),
    path('examlist/',views.examlist, name='examlist'),
    path('examdetail/<str:pk>',views.examdetail, name='examdetail'),
    path('examcreate/', views.examcreate, name='examcreate'),
path('examupdate/<str:pk>',views.examupdate, name='examupdate'),
path('examdelete/<str:pk>',views.examdelete, name='examdelete'),
path('',views.examque, name='examque'),
path('e2',views.examque2, name='examque2'),
path('submit',views.get_mark, name='summit')

    ]

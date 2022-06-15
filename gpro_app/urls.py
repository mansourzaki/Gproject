import imp
from django.urls import path
from . import views 
urlpatterns = [
    path('subjects',views.subjects,name='subjects'),
    path('',views.classes,name='classes'),
    path('lecturers',views.lecturers,name='lecturers'),
    path('yearly',views.yearlyStudents,name='yearlyStudents'),

]
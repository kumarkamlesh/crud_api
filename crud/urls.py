from django.urls import path

from crud.views import *

urlpatterns = [

    path('', EmployeeListView.as_view()),
    path('<int:id>', CrudApiView.as_view()),
]

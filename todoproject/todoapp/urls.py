from django.urls import path
from .import views

urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:taskid>/',views.update,name='update'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.TaskDetailtview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.TaskUpdatetview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TaskDeletetview.as_view(),name='cbvdelete'),
    # path ('details/', views.details, name='details')

]





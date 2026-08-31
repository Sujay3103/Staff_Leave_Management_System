from django.urls import path
from leave.views import apply_leave,my_leaves,view_leave,approve_leave,reject_leave

urlpatterns=[
    path('apply_leave/',apply_leave,name="apply_leave"),
    path('my_leaves/',my_leaves,name="my_leaves"),
    path('view_leave/',view_leave,name='view_leave'),
    path('approve_leave/<int:id>/',approve_leave,name='approve_leave'),
    path('reject_leave/<int:id>,',reject_leave,name='reject_leave')
]
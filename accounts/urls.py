from django.urls import path
from accounts.views import homeview,register,auth,admin_dash,staff_dash,log_out,manage_staff,add_staff,edit_staff,delete_staff

urlpatterns=[
    path("home/",homeview,name='home'),
    path('reg/',register,name="register"),
    path('aut/',auth,name='login'),
    path('admin_dash/',admin_dash,name='admin_dash'),
    path('staff_dash/',staff_dash,name='staff_dash'),
    path('log_out/',log_out,name='log_out'),
    path('manage_staff/',manage_staff,name='manage_staff'),
    path('add_staff/',add_staff,name='add_staff'),
    path('edit_staff/<int:id>/',edit_staff,name='edit_staff'),
    path('delete_staff/<int:id>',delete_staff,name="delete_staff")
]
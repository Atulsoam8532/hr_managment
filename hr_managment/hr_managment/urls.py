"""hr_managment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from managment import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('main/',views.main,name='main'),
    path('login/',views.Login,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('add_proj/',views.add_proj,name='add_proj'),
    path('view_proj/',views.view_proj,name='view_proj'),
    path('add_emplo/',views.add_employe,name='add_emplo'),
    path('view_emplo/',views.view_employe,name='view_emplo'),
    path('apply_leave/',views.apply_leave,name='apply_leave'),
    path('hr_leave_approvel/',views.hr_leave_approval,name='hr_leave_approval'),
    path('hr_leave_approved/<int:id>',views.hr_leave_approved,name='hr_leave_approved'),
    path('hr_leave_reject/<int:id>',views.hr_leave_reject,name='hr_leave_reject'),
    path('manager_leave_approvel/',views.manager_leave_approval,name='manager_leave_approval'),
    path('manager_leave_approved/<int:id>',views.manager_leave_approved,name='manager_leave_approved'),
    path('manager_leave_reject/<int:id>',views.manager_leave_reject,name='manager_leave_reject'),
    path('project/',views.emp_project,name='project'),
    path('manemp/',views.man_emp,name='manemp'),
    path('search/',views.search,name='search'),
    path('view_emp/<int:id>/',views.view_emp,name='view_emp'),
    path('edit_emp/<int:id>/',views.edit_emp,name='edit_emp'),
    path('manager_emp/',views.manager_emp,name='manager_emp')
]

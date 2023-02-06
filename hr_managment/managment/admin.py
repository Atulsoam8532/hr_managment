from django.contrib import admin
from .models import Profiles,eplo_project,leave_manag,Hr_employe,manager_employe

admin.site.register(Profiles)
admin.site.register(eplo_project)
admin.site.register(leave_manag)
admin.site.register(Hr_employe)
admin.site.register(manager_employe)

# Register your models here.

from django.contrib import admin

from .models import Pose

class PoseAdmin(admin.ModelAdmin):
    fields = ['english_name', 'pose_image']
    list_display = ('english_name', 'register_date', 'pose_image')

# Register your models here.
admin.site.register(Pose, PoseAdmin)

from django.contrib import admin
from .models import gallery 
from .models import Services
from .models import videoContent
from .models import contactUs
from embed_video.admin import AdminVideoMixin

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('eventName', 'eventPlace', 'eventDescription', 'eventDate', 'eventImageOne', 'eventImageTwo', 'eventImageThree')

admin.site.register(gallery, ServiceAdmin)



class ServiceEvent(admin.ModelAdmin):
    list_display = ('eventTitle', 'serviceImage')

admin.site.register(Services, ServiceEvent)



class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
   list_display = ('id','eventName', 'eventCaption', 'video')

   
admin.site.register(videoContent, MyModelAdmin)



class contactadmin(admin.ModelAdmin):
    list_display = ('id','name','number','message')

admin.site.register(contactUs, contactadmin)

from django.contrib import admin
from .models import *

admin.site.register(Master)
admin.site.register(Service)
admin.site.register(Schedule)
admin.site.register(Booking)
admin.site.register(Video)
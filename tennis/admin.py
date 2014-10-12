from django.contrib import admin

# Register your models here.
from tennis.models import *

admin.site.register(Court)
admin.site.register(City)
admin.site.register(Province)
admin.site.register(District)

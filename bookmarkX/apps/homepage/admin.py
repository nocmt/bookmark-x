from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Users)
admin.site.register(Sort)
admin.site.register(Bookmarks)
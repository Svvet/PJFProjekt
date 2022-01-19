from django.contrib import admin

from .models import *

admin.site.register(Genre)
admin.site.register(Play)
admin.site.register(Hall)
admin.site.register(Performance)
admin.site.register(Ticket)
admin.site.register(Author)
from django.contrib import admin

# Register your models here.
from facts.models import Artist,Song,Fact

admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Fact)


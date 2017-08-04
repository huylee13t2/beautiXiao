from django.contrib import admin
from app.models import Person, Organisation

class PersonAdmin(admin.ModelAdmin):
	list_display = ['first_name',]

class OrganisationAdmin(admin.ModelAdmin):
	list_display = ['city',]

admin.site.register(Person, PersonAdmin)
admin.site.register(Organisation, OrganisationAdmin)

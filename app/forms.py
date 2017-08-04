from django.forms import ModelForm
from app.models import Organisation, Person, Demo


class PostFormOrganisation(ModelForm):

	class Meta:
		model = Organisation
		fields = ['address_street', 'address_line1', 'address_line2', 'address_line3', 'city', 'region', 'zip_code', 'country', 'mobile_phone', 'mobile_work_phone', 'work_phone', 'email', 'alt_email', 'skype', 'telegram', 'viber', 'whatsapp']


class PostFormPerson(ModelForm):

	class Meta:

		model = Person
		fields = ['accountable_user', 'update_author', 'first_name', 'mid_name', 'last_name', 'organisation', 'address_street', 'address_line1', 'address_line2', 'address_line3', 'city', 'region', 'zip_code', 'country', 'mobile_phone', 'mobile_work_phone', 'work_phone', 'email', 'alt_email', 'skype', 'telegram', 'viber', 'whatsapp']

# 	class Meta:

# 		model = Person
#     	fields = "__all__" 
# 		# fields = ('address_street', 'address_line1', 'address_line2', 'address_line3', 'city', 'region', 'zip_code', 'country', 'mobile_phone', 'mobile_work_phone', 'work_phone', 'email', 'alt_email', 'skype', 'telegram', 'viber', 'whatsapp',) 


# # class PostFormOrganisation(forms.ModelForm):

# # 	class Meta:

# # 		model = Organisation
# # 		fields = ('accountable_user', 'update_author', 'first_name', 'mid_name', 'last_name', 'organisation', 'address_street', 'address_line1', 
# # 			'address_line2', 'address_line3', 'city', 'region', 'zip_code', 'country', 'mobile_phone', 'mobile_work_phone', 'work_phone', 'email', 
# # 			'alt_email', 'skype', 'telegram', 'viber', 'whatsapp',)

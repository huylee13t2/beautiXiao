from django.db import models
from django.contrib.auth.models import User



class Organisation(models.Model):
	# accountable_user = models.ForeignKey(User)
	date_created = models.DateTimeField(u'Date created', null=True)
	date_updated = models.DateTimeField(u'Date updated', auto_now=True, null=True)
	# update_author = models.ForeignKey(User, models.SET_NULL, blank=True, null=True,)
	# first_name = models.CharField(u'User name', max_length=30)
	# mid_name = models.CharField(u'User name', max_length=30)
	# last_name = models.CharField(u'Last name', max_length=30)
	# organisation = models.ForeignKey(Organisations)
	address_street = models.CharField(u'Street', max_length=255, null=True)
	address_line1 = models.CharField(u'Address line 1', max_length=255, null=True)
	address_line2 = models.CharField(u'Address line 2', max_length=255, null=True)
	address_line3 = models.CharField(u'Address line 3', max_length=255, null=True)
	city = models.CharField(u'City', max_length=50, null=True)
	region = models.CharField(u'Region', max_length=50, null=True)
	zip_code = models.CharField(u'Zip code', max_length=50, null=True)
	country = models.CharField(max_length=255, blank=True, null=True)
	mobile_phone = models.CharField(u'Mobile phone', max_length=30, null=True)
	mobile_work_phone = models.CharField(u'Mobile work phone', max_length=30, null=True)
	work_phone = models.CharField(u'Work phone', max_length=30, null=True)
	email = models.CharField(u'E-mail', max_length=50, null=True)
	alt_email = models.CharField(u'Alternative E-mail', max_length=50, null=True)
	skype = models.CharField(u'Skype', max_length=50, null=True)
	telegram = models.CharField(u'Telegram', max_length=50, null=True)
	viber = models.CharField(u'Viber', max_length=50, null=True)
	whatsapp = models.CharField(u'WhatsApp', max_length=50, null=True)

	def __str__(self):
		return u'%s' % self.city


class Person(models.Model):
	accountable_user = models.ForeignKey(User, related_name="person_user", null=True)
	date_created = models.DateTimeField(u'Date created', null=True)
	date_updated = models.DateTimeField(u'Date updated', auto_now=True, null=True)
	update_author = models.ForeignKey(User, models.SET_NULL, blank=True, null=True,)
	first_name = models.CharField(u'User name', max_length=30, null=True)
	mid_name = models.CharField(u'User name', max_length=30, null=True)
	last_name = models.CharField(u'Last name', max_length=30, null=True)
	organisation = models.ForeignKey(Organisation, null=True)
	address_street = models.CharField(u'Street', max_length=255, null=True)
	address_line1 = models.CharField(u'Address line 1', max_length=255, null=True)
	address_line2 = models.CharField(u'Address line 2', max_length=255, null=True)
	address_line3 = models.CharField(u'Address line 3', max_length=255, null=True)
	city = models.CharField(u'City', max_length=50, null=True)
	region = models.CharField(u'Region', max_length=50, null=True)
	zip_code = models.CharField(u'Zip code', max_length=50, null=True)
	country = models.CharField(max_length=255, null=True, blank=True)
	mobile_phone = models.CharField(u'Mobile phone', max_length=30, null=True)
	mobile_work_phone = models.CharField(u'Mobile work phone', max_length=30, null=True)
	work_phone = models.CharField(u'Work phone', max_length=30, null=True)
	email = models.CharField(u'E-mail', max_length=50, null=True)
	alt_email = models.CharField(u'Alternative E-mail', max_length=50, null=True)
	skype = models.CharField(u'Skype', max_length=50, null=True)
	telegram = models.CharField(u'Telegram', max_length=50, null=True)
	viber = models.CharField(u'Viber', max_length=50, null=True)
	whatsapp = models.CharField(u'WhatsApp', max_length=50, null=True)

	def __str__(self):
		return u'%s' % self.first_name

class Demo(models.Model):
	title = models.CharField(max_length=255, null=True)
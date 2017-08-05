from django.shortcuts import render, redirect
from app.forms import PostFormPerson, PostFormOrganisation
from app.models import Organisation, Person

import datetime
from django.utils import timezone

def index(request):

	person = Person.objects.all()
	orgs = Organisation.objects.all()

	return render(request, 'index.html', { 'person' : person, 'orgs' : orgs })


def form_person(request):
	if request.method == 'POST':
		form = PostFormPerson(request.POST)
		if form.is_valid():
			post = form.save(commit = False)
			post.published_date = timezone.now()
			post.save()

			return redirect('index')

	else:

		form = PostFormPerson()

	return render(request, 'form.html', {'form' : form})


def form_org(request):

	if request.method == 'POST':
		form = PostFormOrganisation(request.POST)
		if form.is_valid():
			post = form.save(commit = False)
			post.published_date = timezone.now()
			post.save()

			return redirect('index')

	else:

		form = PostFormOrganisation()

	return render(request, 'form.html', {'form' : form})
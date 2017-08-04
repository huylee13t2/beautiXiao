from django.shortcuts import render
from app.forms import PostFormPerson, PostFormOrganisation

def index(request):

	return render(request, 'index.html', {})


def form_person(request):
	form = PostFormPerson()

	return render(request, 'form.html', {'form' : form})


def form_org(request):
	form = PostFormOrganisation()

	return render(request, 'form.html', {'form' : form})
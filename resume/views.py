from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, request, HttpResponse, JsonResponse
from .forms import ProfileForm
from .models import JobProfile
from django.contrib import messages


# Create your views here.
def home(request):

	return render(request, "accounts/home.html")


def profile(request):


	if request.method == 'POST':

		form = ProfileForm(request.POST, request.FILES)

		if form.is_valid():

			resume = request.FILES['resume']
			bio = form.cleaned_data['bio']
			linkedin = form.cleaned_data['linkedin']
			github = form.cleaned_data['github']
			other_profiles = form.cleaned_data['other_profiles']
			interest = form.cleaned_data['interest']
			experiance = form.cleaned_data['experiance']

			profile_details = JobProfile(user = request.user, resume = resume, bio = bio, linkedin = linkedin, github = github, other_profiles = other_profiles, interest = interest, experiance = experiance)

			profile_details.save()
			messages.success(request, "Thanks for submitting, We will get back to you soon!")
			return redirect("/")

		else:

			messages.success(request, "Fill the form correctly.")
			profile_form = ProfileForm()
			return render(request, "accounts/profile.html", {"profile_form": profile_form})


	else:

		profile_form = ProfileForm()
	
		return render(request, "accounts/profile.html", {"profile_form": profile_form})
					


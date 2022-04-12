from django import forms

INTERSET_CHOICES = [

    ("web-developers", "web-development"),
    ("machine-learning", "machine-learning"),
    ("android-development", "android-development"),
    ("designing", "designing"),
    ("video-editing", "video-editing"),
    ("content-writting", "content-writting"),
    ("marketing", "marketing"),
    ("general", "general"),
    ("competitive programming", "competitive programming"),
]

EXPERIANCE_CHOICES = [('FRESHER', 'FRESHER'), ('1 YEAR', '1 YEAR'), ('2 YEARS', '2 YEARS'), ('3 YEARS', '3 YEARS'), ('5+ YEARS', '5+ YEARS'), ('10+ YEARS', '10+ YEARS')]


class RegisterForm(forms.Form):

    username = forms.CharField(max_length = 255, required=False, label = "Username", widget = forms.TextInput(

    attrs = {

        'class':'form-control',
        'placeholder':'Diary Greenson',

    }))

    pass1 = forms.CharField(max_length = 255, required = True, label = "Password", widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Enter Password', 'type': 'password'}))

    pass2 = forms.CharField(max_length = 255, required = True, label = "Confirm Password", widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Enter Password Again', 'type': 'password'}))



class LoginForm(forms.Form):

	username = forms.CharField(max_length = 255, required=False, label = "Username", widget = forms.TextInput(

	attrs = {

	    'class':'form-control',
	    'placeholder':'Diary Greenson',

	}))

	password = forms.CharField(max_length = 255, required = True, label = "Password", widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Enter Password', 'type': 'password'}))


class ProfileForm(forms.Form):

	resume = forms.FileField()
	bio = forms.CharField(max_length = 3000, required = True, label = "Bio*", widget = forms.TextInput(attrs = {'class': 'form-control m-2', 'placeholder': 'Describe Yourself in short', 'row': '4', 'col': '30'}))
	linkedin = forms.CharField(max_length = 1000, required = False, label = "LinkedIn Profile(Optional)", widget = forms.TextInput(attrs = {'class': 'form-control m-2', 'placeholder': 'Enter LinkedIn Profile'}))
	github = forms.CharField(max_length = 1000, required = False, label = "Github Profile(Optional)", widget = forms.TextInput(attrs = {'class': 'form-control m-2', 'placeholder': 'Enter LinkedIn Profile'}))
	other_profiles = forms.CharField(max_length = 1000, required = False, label = "Other Profiles(Optional)", widget = forms.TextInput(attrs = {'class': 'form-control m-2', 'placeholder': 'Enter Other Profiles'}))

	interest = forms.ChoiceField(choices = INTERSET_CHOICES, widget = forms.Select(attrs = {'class': 'form-control m-2', 'placeholder': 'Enter Password'}))
	experiance = forms.ChoiceField(choices = EXPERIANCE_CHOICES, widget = forms.Select(attrs = {'class': 'form-control m-2', 'placeholder': 'Enter Password'}))
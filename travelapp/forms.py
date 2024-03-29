from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import City, Flights,Hotels,BookPackage,BookFlight,BookHotel,Famous
import datetime


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    last_name = forms.CharField(max_length=30,widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    username = forms.CharField(max_length=254,widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    password1=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'class':'d-form form-control'}))
    password2=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'class':'d-form form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
    def clean(self):
        cleaned_data = super(UserCreationForm, self).clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254,widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    password = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'class':'d-form form-control'}))

    class Meta:
        model = User

class FlightForm(forms.Form):
    source = forms.CharField(max_length=20,label='SOURCE',widget=forms.TextInput(attrs={'class' : 'fs-form form-control','placeholder':'Source'}),required=False)
    destination = forms.CharField(max_length=20,label='DESTINATION',widget=forms.TextInput(attrs={'class' : 'fds-forms form-control','placeholder':'Destination'}),required=False)
    date = forms.DateField(initial=datetime.date.today,label='DATE',widget=forms.TextInput(attrs={'class' : 'fd-form form-control','placeholder':'YYYY-MM-DD'}),required=False)

    class Meta:
        model = Flights
        fields = ('source','destination','city')


class HotelForm(forms.Form):
    city = forms.CharField(max_length=20,label='CITY',widget=forms.TextInput(attrs={'class' : 'fs-form form-control','placeholder':'City'}),required=False)
    date = forms.DateField(initial=datetime.date.today,label='Date ',widget=forms.TextInput(attrs={'class' : 'fd-form form-control','placeholder':'YYYY-MM-DD'}),required=False)

    class Meta:
        model = Hotels
        fields = ('city')

class ChoiceForm(forms.Form):
    flight = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class' : 'fs-form form-control','placeholder':'Choose Flight'}),required=False)
    seats = forms.IntegerField(widget=forms.TextInput(attrs={'class' : 'fs-form form-control','placeholder':'SEATS'}),required=False)
    hotel = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class' : 'fs-form form-control','placeholder':'Choose Hotel'}),required=False)
    rooms = forms.IntegerField(widget=forms.TextInput(attrs={'class' : 'fs-form form-control','placeholder':'ROOMS'}),required=False)

    class Meta:
        models = BookPackage
        fields = ('flight','seat','hotel_name','room')

class SeatForm(forms.Form):
    seats = forms.IntegerField(widget=forms.TextInput(attrs={'class' : 'fs-form form-control','placeholder':'SEATS'}),required=False)

    class Meta:
        models = BookFlight
        fields = ('seats')

class RoomForm(forms.Form):
    rooms = forms.IntegerField(widget=forms.TextInput(attrs={'class' : 'fs-form form-control','placeholder':'ROOMS'}),required=False)

    class Meta:
        models = BookHotel
        fields = ('room')

class CityForm(forms.Form):
    city = forms.CharField(max_length=20,label='CITY',widget=forms.TextInput(attrs={'class' : 'fs-form form-control','placeholder':'City'}),required=False)

    class Meta:
        models = Famous

# forms.py
from django import forms
from .models import Famous

class FamousForm(forms.ModelForm):
    class Meta:
        model = Famous
        fields = ['city', 'place_name', 'image', 'desc']
# forms.py
from django import forms
from .models import Hotels

class HotelsForm(forms.ModelForm):
    class Meta:
        model = Hotels
        fields = '__all__'  # You can also specify the fields you want to include

class FlightsForm(forms.ModelForm):
    class Meta:
        model = Flights
        fields = '__all__'
        widgets = {
            'dept_time': forms.TimeInput(attrs={'type': 'time'}),
            'dest_time': forms.TimeInput(attrs={'type': 'time'}),
        }

class CityForm(forms.Form):
    city = forms.CharField(max_length=20,label='CITY',widget=forms.TextInput(attrs={'class' : 'fs-form form-control','placeholder':'City'}),required=False)

    class Meta:
        models = Famous

class CityForm2(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'
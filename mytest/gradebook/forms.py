from django import forms
import datetime
from django.forms import widgets
from gradebook.models import Address, Student


class StudentForm(forms.ModelForm):
    student_last_name = forms.CharField(max_length=225, help_text="Last Name")
    student_first_name = forms.CharField(max_length=225, help_text="First Name")
    student_alternative_name = forms.CharField(max_length=45, required=False, help_text="Alternative Names")
    student_birth_date = forms.DateField(required=False, help_text="Birth Date")
    student_email = forms.EmailField(max_length=225, required=False, help_text="Email")
    student_phone = forms.CharField(max_length=225, required=False, help_text="Phone Number")
    addresses_address_id = forms.ModelChoiceField(queryset=Address.objects.all())

    class Meta:
        model = Student
        fields = ('student_last_name', 'student_first_name', 'student_alternative_name', 'student_birth_date',
                  'student_email', 'student_phone')


class AddressForm(forms.ModelForm):
    address_street_1 = forms.CharField(max_length=128, help_text="Street Address 1")
    address_street_2 = forms.CharField(max_length=128, help_text="Street Address 2", required=False)
    address_city = forms.CharField(max_length=128, help_text="City")
    address_state = forms.CharField(max_length=2, help_text="State")
    address_zip = forms.CharField(max_length=128, help_text="ZIP")
    address_country = forms.CharField(max_length=128, help_text="Country")

    class Meta:
        model = Address
        fields = ('address_street_1', 'address_street_2', 'address_city', 'address_state', 'address_zip',
                  'address_country')
        exclude = ('Student',)
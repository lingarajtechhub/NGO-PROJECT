from django import forms
from .models import WidowProfile

class WidowProfileForm(forms.ModelForm):
    class Meta:
        model = WidowProfile
        fields = '__all__'
        labels = {
            'project_name': 'Select Project Location',
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'case_history': forms.Textarea(attrs={'rows': 4}),
            'dependents': forms.RadioSelect,
            'address': forms.Textarea(attrs={'rows': 4}),
            'cause_of_death': forms.TextInput(attrs={'size': 50}),
            'death_certificate': forms.CheckboxInput,
            'death_certificate_file': forms.FileInput(attrs={'accept': 'image/jpeg,image/png,application/pdf'}),
            'aadhar_card': forms.CheckboxInput,
            'aadhar_card_file': forms.FileInput(attrs={'accept': 'image/jpeg,image/png,application/pdf'}),
            'application': forms.CheckboxInput,
            'application_file': forms.FileInput(attrs={'accept': 'image/jpeg,image/png,application/pdf'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        dependents = cleaned_data.get('dependents')
        dependents_name = cleaned_data.get('dependents_name')
        dependents_age = cleaned_data.get('dependents_age')
        dependents_sex = cleaned_data.get('dependents_sex')
        death_certificate = cleaned_data.get('death_certificate')
        death_certificate_file = cleaned_data.get('death_certificate_file')
        aadhar_card = cleaned_data.get('aadhar_card')
        aadhar_card_file = cleaned_data.get('aadhar_card_file')
        application = cleaned_data.get('application')
        application_file = cleaned_data.get('application_file')

        # Validate dependents fields
        if dependents == 'Yes':
            if not dependents_name:
                self.add_error('dependents_name', 'Dependents name is required when dependents is Yes.')
            if not dependents_age:
                self.add_error('dependents_age', 'Dependents age is required when dependents is Yes.')
            if not dependents_sex:
                self.add_error('dependents_sex', 'Dependents sex is required when dependents is Yes.')
        else:
            # Clear dependents fields if "No" is selected
            cleaned_data['dependents_name'] = ''
            cleaned_data['dependents_age'] = None
            cleaned_data['dependents_sex'] = ''

        # Validate death certificate file
        if death_certificate and not death_certificate_file:
            self.add_error('death_certificate_file', 'Death certificate file is required when death certificate is checked.')
        elif not death_certificate:
            cleaned_data['death_certificate_file'] = None

        # Validate Aadhar card file
        if aadhar_card and not aadhar_card_file:
            self.add_error('aadhar_card_file', 'Aadhar card file is required when Aadhar card is checked.')
        elif not aadhar_card:
            cleaned_data['aadhar_card_file'] = None

        # Validate application file
        if application and not application_file:
            self.add_error('application_file', 'Application file is required when application is checked.')
        elif not application:
            cleaned_data['application_file'] = None

        return cleaned_data
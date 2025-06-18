from django.db import models

class WidowProfile(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    NATIONALITY_CHOICES = [
        ('Indian', 'Indian'),
    ]
    RELIGION_CHOICES = [
        ('Hindu', 'Hindu'),
        ('Christian', 'Christian'),
        ('Muslim', 'Muslim'),
    ]
    DEPENDENTS_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    registration_number = models.CharField(max_length=50, unique=True)
    date = models.DateField()
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    spouse_name = models.CharField(max_length=100)
    cause_of_death = models.CharField(max_length=200)
    nationality = models.CharField(max_length=50, choices=NATIONALITY_CHOICES, default='Indian')
    religion = models.CharField(max_length=50, choices=RELIGION_CHOICES)
    address = models.TextField()
    contact_phone = models.CharField(max_length=15)
    case_history = models.TextField()
    dependents = models.CharField(max_length=3, choices=DEPENDENTS_CHOICES, default='No')
    dependents_name = models.CharField(max_length=100, default="", blank=True, null=True)
    dependents_age = models.IntegerField(blank=True, null=True)
    dependents_sex = models.CharField(max_length=50, default="", blank=True, null=True)
    death_certificate = models.BooleanField(default=False)
    death_certificate_file = models.FileField(upload_to='death_certificates/', blank=True, null=True)
    aadhar_card = models.BooleanField(default=False)
    aadhar_card_file = models.FileField(upload_to='aadhar_cards/', blank=True, null=True)
    aadhar_number = models.CharField(max_length=12, blank=True)
    letter_from_sarpanch = models.BooleanField(default=False)
    application = models.BooleanField(default=False)
    application_file = models.FileField(upload_to='applications/', blank=True, null=True)
    emergency_contact = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    class Meta:
        db_table = 'ngo_data'

    def __str__(self):
        return self.name
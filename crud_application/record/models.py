from django.db import models

# Create your models here.

class Users(models.Model):
    gender_field = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    language_field =[
        ('nepali', 'Nepali'),
        ('english', 'English'),
        ('chinese', 'Chinese')
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    gender = models.CharField(choices=gender_field, max_length=10)
    language = models.CharField(choices=language_field, max_length=100)
    country = models.CharField(max_length=100)
    image = models.ImageField(upload_to='user_gallery', blank=True, null=True)

    def get_language(self):
        lang = self.language
        lang_object = lang.split(',')
        return lang_object
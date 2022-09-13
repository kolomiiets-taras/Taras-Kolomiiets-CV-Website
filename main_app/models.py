from datetime import date

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator


class Profile(models.Model):
    profile_img = models.ImageField(blank=True, null=True, upload_to="images/")
    first_name = models.CharField(blank=False, max_length=200)
    last_name = models.CharField(blank=False, max_length=200)
    about_you = models.TextField(blank=True, max_length=1000)
    phone = PhoneNumberField(null=True, blank=False, unique=True)
    email = models.EmailField(max_length=200, null=True, blank=False, unique=True)
    linkedIn_link = models.CharField(blank=True, max_length=200)
    gitHub_link = models.CharField(blank=True, max_length=200)
    facebook_link = models.CharField(blank=True, max_length=200)

    @property
    def get_img_url(self):
        try:
            url = self.profile_img.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Education(models.Model):
    CHOICES = (
        ('Bachelor', 'Bachelor'),
        ('Master', 'Master'),
    )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    institution = models.CharField(blank=False, max_length=200)
    course_name = models.CharField(blank=False, max_length=200)
    certificate = models.ImageField(blank=True, null=True, upload_to="images/")
    degree = models.CharField(choices=CHOICES, max_length=100, blank=True)
    date_start = models.DateField()
    date_end = models.DateField()

    @property
    def get_img_url(self):
        try:
            url = self.certificate.url
        except:
            url = ''
        return url

    @property
    def is_future(self):
        return date.today() < self.date_end

    def __str__(self):
        return self.course_name


class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    project_name = models.CharField(blank=True, max_length=200)
    description = models.TextField(blank=True, max_length=1000)
    gitHub_link = models.CharField(blank=True, max_length=200)
    link = models.CharField(blank=True, max_length=200)

    @property
    def first_image(self):
        return self.projectimage_set.first()

    def __str__(self):
        return self.project_name


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=False, null=True)
    project_img = models.ImageField(blank=False, null=True, upload_to="images/")

    @property
    def get_img_url(self):
        try:
            url = self.project_img.url
        except:
            url = ''
        return url


class TechSkill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    skill_name = models.CharField(blank=False, max_length=200)
    level = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(0)])

    def __str__(self):
        return self.skill_name


class Language(models.Model):
    CHOICES = (
        ('A1', "A1"),
        ('A2', "A2"),
        ('B1', "B1"),
        ('B2', "B2"),
        ('C1', "C1"),
        ('C2', "C2"),
        ('Native', "Native"))
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    lang_name = models.CharField(blank=False, max_length=200)
    level = models.CharField(choices=CHOICES, max_length=100, blank=False)

    def __str__(self):
        return self.lang_name


class Resume(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, blank=True, null=True)
    resume = models.FileField(blank=False, null=True, upload_to="files/")

    @property
    def get_resume_url(self):
        try:
            url = self.resume.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.profile.__str__() + ' resume'



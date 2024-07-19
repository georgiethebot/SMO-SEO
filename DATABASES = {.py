DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class Obituary(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    content = models.TextField()
    author = models.CharField(max_length=100)
    submission_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + "-" + str(self.date_of_death))
        super().save(*args, **kwargs)
from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class Obituary(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    content = models.TextField()
    author = models.CharField(max_length=100)
    submission_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + "-" + str(self.date_of_death))
        super().save(*args, **kwargs)
from django.shortcuts import render, redirect
from .models import Obituary
from .forms import ObituaryForm

def submit_obituary(request):
    if request.method == 'POST':
        form = ObituaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_obituaries')
    else:
        form = ObituaryForm()
    return render(request, 'obituaries/obituary_form.html', {'form': form})
from django import forms
from .models import Obituary

class ObituaryForm(forms.ModelForm):
    class Meta:
        model = Obituary
        fields = ['name', 'date_of_birth', 'date_of_death', 'content', 'author']
from django.shortcuts import render
from .models import Obituary

def view_obituaries(request):
    obituaries = Obituary.objects.all()
    return render(request, 'obituaries/view_obituaries.html', {'obituaries': obituaries})
from django.contrib.sitemaps import Sitemap
from .models import Obituary


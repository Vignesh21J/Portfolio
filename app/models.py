from django.db import models

# Create your models here.

class Home(models.Model):
    name = models.CharField(max_length=20)
    greetings_1 = models.CharField(max_length=10)
    greetings_2 = models.CharField(max_length=10)
    picture = models.ImageField(upload_to='picture/')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}. {self.name}'
    
class About(models.Model):
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=50)
    description  = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career
    
class Profile(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name="profiles")
    social_name = models.CharField(max_length=20)
    link = models.URLField(max_length=200)
    icon_class = models.CharField(max_length=50, default='')  # For storing icon class.

    def __str__(self):
        return self.social_name
    
class Category(models.Model):
    name = models.CharField(max_length=25)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name

class Skills(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=20)


class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=200)

    def __str__(self):
        return f'Portfolio {self.id}'

class ContactFormLog(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    action_time = models.DateTimeField(null = True, blank = True)
    is_success = models.BooleanField(default=False)
    is_error = models.BooleanField(default=False)

    error_message = models.TextField(null = True,  blank = True)

    def __str__(self):
        return self.email
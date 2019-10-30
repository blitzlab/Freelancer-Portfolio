from django.db import models

# Create your models here.
class Freelancer(models.Model):
    first_name = models.CharField(max_length = 200, blank = True)
    last_name = models.CharField(max_length = 200, blank = True)
    title = models.CharField(max_length = 200, default = 'Web Developer')
    avater = models.ImageField(upload_to = 'avater', null = True)
    about = models.TextField(blank = True)
    address = models.CharField(max_length = 500, blank = True)

    def __str__(self):
        return self.first_name+' '+self.last_name

class Skill(models.Model):
    SKILL = [
        ('HTML', 'HTML'),
        ('CSS', 'CSS'),
        ('JAVASCRIPT', 'JAVASCRIPT'),
        ('PYTHON', 'PYTHON'),
        ('DJANGO', 'DJANGO'),
        ('WORDPRESS', 'WORDPRESS'),
        ('PHP', 'PHP'),
    ]
    freelancer = models.ForeignKey(Freelancer, related_name = 'skills', on_delete = models.CASCADE)
    choice = models.CharField(max_length = 50, choices = SKILL, blank = True)

    def __str__(self):
        return self.choice

class Portfolio(models.Model):
    freelancer = models.ForeignKey(Freelancer, related_name = 'portfolio', on_delete = models.CASCADE)
    title = models.CharField(max_length = 200, blank = True)
    image = models.ImageField(upload_to = 'portfolio_image', null = True)
    about = models.TextField(blank = True)

    def __str__(self):
        return self.title

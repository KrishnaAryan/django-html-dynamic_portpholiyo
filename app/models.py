from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class FirstPage(models.Model):
    name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='media/profile_image')
    role=models.CharField(max_length=150)
    about_short=models.CharField(max_length=150)
    facebook_url=models.CharField(max_length=2000, null=True, blank=True)
    twitter_link=models.CharField(max_length=2000,null=True, blank=True)
    linkedln_link=models.CharField(max_length=2000,null=True,blank=True)
    instagram_link=models.CharField(max_length=2000,null=True,blank=True)
    
    def __str__(self):
        return self.name + "--" + self.role
    
class About(models.Model):
    profession=models.CharField(max_length=50)
    heading=models.CharField(max_length=70)
    description=models.TextField()
    photo=models.ImageField('media/about_photo',null=True)
    experience=models.IntegerField()
    number_of_project=models.IntegerField()
    
    def __str__(self):
        return self.profession + "--" + str(self.experience )
    
class Portfolio(models.Model):
    feature_image=models.ImageField(upload_to='media/portfolio/images')
    heading=models.CharField(max_length=70)
    description = RichTextField()
    photo=models.ImageField(upload_to='media/portfolio/images')
    def __str__(self):
        return self.heading
    
class PortfolioIimage(models.Model):
    chose=models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    your_images=models.ImageField(upload_to='media/portfolio/images')
    
class Skill(models.Model):
    chose=models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    skill=models.CharField(max_length=200)
    level=models.IntegerField()
    def __str__(self):
        return self.skill + "--" + str(self.level)
    
class Experience(models.Model):
    company_logo=models.ImageField(upload_to='media/company/images')
    company_nane=models.CharField(max_length=100)
    job_role=models.CharField(max_length=100)
    start_and_end_Date=models.CharField(max_length=20)
    about_job=RichTextField()
    roles_and_responsibilities=RichTextField()
    def __str__(self):
        return self.company_nane + "--" + self.job_role + "--" + self.start_and_end_Date
    
class Blog(models.Model):
    image=models.ImageField(upload_to='media/portfolio/blog')
    date=models.CharField(max_length=10)
    name=models.CharField(max_length=100)
    about=models.CharField(max_length=200)
    write_your_blog=RichTextField()
    def __str__(self):
        return self.name + "--" + self.date
    
class YourContactInfo(models.Model):
    address=models.TextField()
    email=models.EmailField()
    phone_number=models.CharField(max_length=15)
    
    def __str__(self):
        return self.address + "--" + self.email + "--" + self.phone_number


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name + "--" + self.email + "--" + self.phone + "--" + self.subject
 
 
 
class Resume(models.Model):
    upload_resume=models.FileField(upload_to='media/Resume')
    def __str__(self):
        return self.upload_resume
     
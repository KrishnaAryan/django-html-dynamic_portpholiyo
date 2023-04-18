from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(FirstPage)
admin.site.register(About)




class PortfolioIimage(admin.TabularInline):
    model = PortfolioIimage

class Skill(admin.TabularInline):
    model = Skill

class PortfolioAdmin(admin.ModelAdmin):
    inlines = (PortfolioIimage,Skill)

admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Experience)
admin.site.register(Blog)
admin.site.register(YourContactInfo)
admin.site.register(Contact)
admin.site.register(Resume)

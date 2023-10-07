from django.contrib import admin
from admissions.models import School
from admissions.models import teacher

# Register your models here.
#class StudentAdmin(admin.ModelAdmin):
 #   list_display=['id','name','founded_year','location']
class student(admin.ModelAdmin):
    list_display=['id','name','location','founded_year']

class teacheradmin(admin.ModelAdmin):
    list_display=['id','name','exp','subject']

admin.site.register(School,student)
admin.site.register(teacher,teacheradmin)
from django.contrib import admin
from . models import Book_ticket

# Register your models here.
@admin.register(Book_ticket)
class Book_tickeAdmin(admin.ModelAdmin):
    list_display=('boofrom','bookTo','dep_date')
	

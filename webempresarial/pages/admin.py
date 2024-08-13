from django.contrib import admin

from pages.models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'order')
    

admin.site.register(Page, PageAdmin)
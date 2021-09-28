from django.contrib import admin

# Register your models here.
from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'birthdate',
        'email',
    ]

    list_display_links = list_display
    list_per_page = 10

    fields = [
        ('first_name', 'last_name'),
        ('birthdate', 'age'),
        'email',
        ('enroll_date', 'graduate_date', 'graduate_date2'),
        'group',
    ]

    readonly_fields = ['age']
    search_fields = ['first_name', 'last_name']
    list_filter = ['age']


admin.site.register(User, UserAdmin)

from django.contrib import admin

from .models import Hello


class HelloAdmin(admin.ModelAdmin):
    model = Hello


admin.site.register(Hello, HelloAdmin)

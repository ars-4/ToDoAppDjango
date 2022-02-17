from django.contrib import admin
from core.models import Notes

# Register your models here.

RegisteredModels = [
    Notes,
]

admin.site.register(RegisteredModels)
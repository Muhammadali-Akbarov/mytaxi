from django.contrib import admin
from .models import Order,Client,Driver

admin.site.register([Order,Client,Driver])

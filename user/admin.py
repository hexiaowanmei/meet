from django.contrib import admin

# Register your models here.
# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.contrib import admin
from user.models import *

# Register your models here.

admin.site.register(User)
# admin.site.register(HeroInfo)


class UserAdmin(admin.ModelAdmin):
    list_display = ['id']
from django.contrib import admin

# Register your models here.

from learning_app.models import Topic
admin.site.register(Topic)

from  learning_app.models import Entry
admin.site.register(Entry)
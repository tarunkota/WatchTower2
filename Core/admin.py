from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Frequency)
admin.site.register(Project)
admin.site.register(Metric)
admin.site.register(Module)


class MetricValueAdmin(admin.ModelAdmin):
    list_filter = ['metric']


admin.site.register(MetricValue, MetricValueAdmin)

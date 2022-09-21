import requests
import json
from .models import *


def saveMetricData(metric, data):
    mv = MetricValue(metric=metric,
                     intValue=data.get('intValue', None),
                     strValue=data.get('strValue', None))
    mv.save()


def getMetricValue(metric):
    """Get metric value and save in db

    Args:
        metric (Metric): Metric
    """
    r = requests.get(metric.endpoint, headers={
                     'Authorization': metric.project.authToken})
    data = json.loads(r.text)
    saveMetricData(metric, data)


def getModuleValues(module):
    """Get and save all metrics of a module

    Args:
        module (_type_): _description_
    """
    r = requests.get(module.endpoint, headers={
                     'Authorization': module.project.authToken})
    data = json.loads(r.text)
    metricsData = data.get("metrics", [])
    for mdata in metricsData:
        metric = Metric.objects.get(project=module.project, name=mdata['name'])
        if (metric.frequency.frequencyInSeconds >= module.frequency.frequencyInSeconds):
            saveMetricData(metric, mdata)


def getAllMetricValues(frequency):
    """Get all metric values of a given frequency

    Args:
        frequency (Frequenct): Frequency
    """
    metrics = Metric.objects.filter(frequency=frequency)
    for metric in metrics:
        getMetricValue(metric)


def getAllModuleValues(frequency):
    """Get all metric values of a given frequency

    Args:
        frequency (Frequenct): Frequency
    """
    modules = Module.objects.filter(frequency=frequency)
    for module in modules:
        getModuleValues(module)

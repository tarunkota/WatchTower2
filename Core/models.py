from django.db import models
from django.utils.timezone import localtime


class Frequency(models.Model):
    """Frequency at which to fetch values metrics or modules.
    """
    name = models.CharField(max_length=64)
    frequencyInSeconds = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Project(models.Model):
    """Projects the watch tower monitors.
    """
    name = models.TextField()
    authToken = models.TextField()

    def __str__(self):
        return self.name


class Metric(models.Model):
    """Metric is a data which we monitor
    """
    project = models.ForeignKey(
        Project, related_name='metrics', on_delete=models.CASCADE)
    name = models.TextField()
    endpoint = models.URLField()
    frequency = models.ForeignKey(
        Frequency, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project)+" "+str(self.name)


class MetricValue(models.Model):
    """Value of a metric at a certain instant.

    Args:
        models (_type_): _description_
    """
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE)
    intValue = models.IntegerField(null=True)
    strValue = models.TextField(null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.metric)+" "+str(localtime(self.created))


class Module(models.Model):
    """A collection of metrics/modules.
    """
    project = models.ForeignKey(
        Project, related_name='modules', on_delete=models.CASCADE)
    name = models.TextField()
    endpoint = models.URLField()

    metrics = models.ManyToManyField(Metric)
    frequency = models.ForeignKey(
        Frequency, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.project)+" "+str(self.name)

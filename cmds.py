from Core.crons import *
from Core.tasks import *
metric = Metric.objects.get(pk=1)
# getMetricValue(metric)
# getAllMetricValues(metric.frequency)
# getAllModuleValues(metric.frequency)
getAllModuleValues(Frequency.objects.get(pk=2))


everyMinuteCron()

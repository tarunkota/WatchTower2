from .models import Frequency
from .tasks import getAllMetricValues, getAllModuleValues


def everyMinuteCron():
    """
    """
    frequency = Frequency.objects.get(pk=2)
    getAllMetricValues(frequency)
    getAllModuleValues(frequency)


def every10MinuteCron():
    """
    """
    frequency = Frequency.objects.get(pk=3)
    getAllMetricValues(frequency)
    getAllModuleValues(frequency)


def everyHourCron():
    """
    """
    frequency = Frequency.objects.get(pk=4)
    getAllMetricValues(frequency)
    getAllModuleValues(frequency)


def every6HoursCron():
    """
    """
    frequency = Frequency.objects.get(pk=5)
    getAllMetricValues(frequency)
    getAllModuleValues(frequency)


def every12HoursCron():
    """
    """
    frequency = Frequency.objects.get(pk=6)
    getAllMetricValues(frequency)
    getAllModuleValues(frequency)


def every24HoursCron():
    """
    """
    frequency = Frequency.objects.get(pk=7)
    getAllMetricValues(frequency)
    getAllModuleValues(frequency)

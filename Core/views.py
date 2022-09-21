from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from .models import Project, Metric, MetricValue, Module
from .serializers import MetricValueSerializer
# Create your views here.


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getMetricValues(request):
    pname = request.GET.get("project")
    mname = request.GET.get("metric")
    count = int(request.GET.get("count", '1'))
    print(request.GET)
    print(mname)

    project = Project.objects.get(name=pname)
    metric = Metric.objects.get(name=mname)
    metricValues = MetricValue.objects.filter(
        metric=metric).order_by('-created')[0:count]

    data = MetricValueSerializer(metricValues, many=True).data
    return JsonResponse({"data": data})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getModuleValues(request):
    pname = request.GET.get("project")
    mname = request.GET.get("module")

    project = Project.objects.get(name=pname)
    module = Module.objects.get(project=project, name=mname)
    metrics = module.metrics.all()

    data = []
    for metric in metrics:
        mv = MetricValue.objects.filter(metric=metric).order_by('-created')[0]
        data.append(MetricValueSerializer(mv, many=False).data)

    return JsonResponse({"data": data})

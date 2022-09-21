from rest_framework import serializers
from .models import *


class MetricSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Metric
        fields = ['name']


class MetricValueSerializer(serializers.HyperlinkedModelSerializer):

    metric = serializers.SerializerMethodField()

    class Meta:
        model = MetricValue
        fields = ['intValue', 'strValue', 'created', 'metric']

    def get_metric(self, obj):
        return MetricSerializer(obj.metric, many=False).data

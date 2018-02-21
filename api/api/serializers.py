from rest_framework import serializers
from .models import Topic, Resource, Position, Publisher


class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = ('url', 'name')


class ResourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resource
        fields = ('publisher', 'resource_url')


class PositionSerializer(serializers.HyperlinkedModelSerializer):
    resources = ResourceSerializer(many=True)

    class Meta:
        model = Position
        fields = ('resources',)


class PositionSummarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = ('url', 'summary', 'summary_source')


class TopicSerializer(serializers.HyperlinkedModelSerializer):
    position = PositionSerializer(read_only=True)
    positions = PositionSummarySerializer(many=True, read_only=True)
    summary_source = ResourceSerializer()

    class Meta:
        model = Topic
        fields = ('url', 'summary', 'summary_source',
                  'related_topics', 'position', 'positions')

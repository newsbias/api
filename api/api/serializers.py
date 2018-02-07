from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.api.models import Source, Article, Metric


class MetricSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Metric
        fields = ('metric_type', 'metric_value')


class SourceWithoutArticlesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Source
        fields = ('url', 'name')


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    publisher = SourceWithoutArticlesSerializer(read_only=True)
    metrics = MetricSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ('url', 'title', 'article_url',
                  'cleaned_text', 'cleaned_html', 'publisher',
                  'metrics')


class SourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Source
        fields = ('url', 'name', 'articles')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

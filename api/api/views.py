from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.api.serializers import (
        UserSerializer, GroupSerializer, ArticleSerializer,
        SourceSerializer, MetricSerializer)
from api.api.models import Article, Source, Metric


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint allowing users to be viewed or edited
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint allowing groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint allowing articles to be viewed or edited
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class SourceViewSet(viewsets.ModelViewSet):
    """
    API endpoint allowing sources to be viewed or edited
    """
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


# TODO a different ViewSet would be better
class MetricViewSet(viewsets.ModelViewSet):
    """
    API endpoint allowing metrics to be viewed or edited
    """
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer

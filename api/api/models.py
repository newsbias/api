from django.db import models


class Source(models.Model):
    name = models.CharField(max_length=32)


class Article(models.Model):
    title = models.CharField(max_length=64)
    article_url = models.URLField()
    cleaned_text = models.CharField(max_length=2048)
    cleaned_html = models.CharField(max_length=4096)
    publisher = models.ForeignKey(Source, related_name='articles',
                                  on_delete=models.CASCADE)


class Metric(models.Model):
    METRIC_TYPES = (
        (0, 'Sentiment'),
        (1, 'Reading time'),
        # TODO
    )
    article = models.ForeignKey(Article, related_name='metrics',
                                on_delete=models.CASCADE)
    metric_type = models.IntegerField(choices=METRIC_TYPES)
    metric_value = models.FloatField()

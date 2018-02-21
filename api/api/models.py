from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=1024)

    def __str__(self):
        return str(self.name)


class Resource(models.Model):
    resource_url = models.CharField(max_length=1024)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(str(self.publisher), str(self.resource_url))


class Position(models.Model):
    resources = models.ManyToManyField(Resource)


class Topic(models.Model):
    summary = models.CharField(max_length=1024)
    summary_source = models.ForeignKey(Resource, on_delete=models.CASCADE)
    related_topics = models.ManyToManyField('self', blank=True)
    position = models.OneToOneField(
            Position, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.summary)

    def positions(self):
        return self.related_topics.filter(position__isnull=False)

    def is_position(self):
        return self.position is not None

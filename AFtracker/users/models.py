from django.db import models


class Crew(models.Model):
    work_center = models.CharField(max_length=50, null=True, blank=True)
    crew_name = models.CharField(
        max_length=50, default='new crew', null=True, blank=True)
    crew_size = models.IntegerField(default=1, null=True, blank=True)

    def __str__(self):
        return (self.crew_name)

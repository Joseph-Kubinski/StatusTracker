from django.db import models


class Crew(models.Model):
    work_center = models.CharField(max_length=50)
    crew_size = models.IntegerField(default=1)

    def __str__(self):
        return (self.work_center)

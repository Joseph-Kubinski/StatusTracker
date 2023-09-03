from django.db import models


class Crew(models.Model):
    workplace = models.ForeignKey('WorkCenter',
                                  on_delete=models.CASCADE, default=None, null=True, blank=True)
    crew_name = models.CharField(
        max_length=50, default='new crew', null=True, blank=True)
    crew_size = models.IntegerField(default=1, null=True, blank=True)

    def __str__(self):
        return (str(self.workplace) + " " + str(self.crew_name))


class WorkCenter(models.Model):
    name = models.CharField(max_length=255)
    squadron = models.ForeignKey('Squadron',
                                 on_delete=models.CASCADE, default=None, null=True, blank=True)
    crews = models.ForeignKey('Crew',
                              on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        return (self.name)


class Squadron(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return (self.name)

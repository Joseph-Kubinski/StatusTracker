from django.db import models


AMC_CHOICES = [('INW', "In-work"),
               ('INW-X', "In-work, no addtional crews permitted"),
               ('AWM-1', "Awaiting Maintenance Code 1"),
               ('AWM-2', "Awaiting Maintenance Code 2"),
               ('AWM-3', "Awaiting Maintenance Code 3"),
               ('AWP', "Awaiting Parts"),
               ('RDY', "Ready for Lines, No MX required")]

AMS_CHOICES = [('NMC', "Not Mission Capable"),
               ('PMC', "Partially Mission Capable"),
               ('FMC', 'Fully Mission Capable')]


class Acft(models.Model):
    tail_number = models.CharField(max_length=10)

    acft_mx_status = models.CharField(
        max_length=255, choices=AMS_CHOICES, default=None, null=True, blank=True)
    acft_mission_status = models.CharField(
        max_length=255, choices=AMC_CHOICES, default=None, null=True, blank=True)
    crews_assigned = models.ForeignKey(
        'Crew',
        on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        return (self.tail_number)


class Crew(models.Model):
    work_center = models.CharField(max_length=50)
    crew_size = models.IntegerField(default=1)

    def __str__(self):
        return (self.work_center)

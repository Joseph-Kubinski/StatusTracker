from django.db import models


class Acft(models.Model):
    tail_number = models.CharField(max_length=10)
    acft_mission_status = [('NMC', "Not Mission Capable"),
                           ('PMC', "Partially Mission Capable"),
                           ('FMC', 'Fully Mission Capable')]
    acft_mx_status = [('INW', "In-work"),
                      ('INW-X', "In-work, no addtional crews permitted"),
                      ('AWM-1', "Awaiting Maintenance Code 1"),
                      ('AWM-2', "Awaiting Maintenance Code 2"),
                      ('AWM-3', "Awaiting Maintenance Code 3"),
                      ('AWP', "Awaiting Parts"),
                      ('RDY', "Ready for Lines, No MX required")]

# Generated by Django 4.0 on 2023-09-03 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acft', '0003_acft_crews_assigned'),
    ]

    operations = [
        migrations.AddField(
            model_name='acft',
            name='acft_mx_status',
            field=models.CharField(blank=True, choices=[('INW', 'In-work'), ('INW-X', 'In-work, no addtional crews permitted'), ('AWM-1', 'Awaiting Maintenance Code 1'), ('AWM-2', 'Awaiting Maintenance Code 2'), ('AWM-3', 'Awaiting Maintenance Code 3'), ('AWP', 'Awaiting Parts'), ('RDY', 'Ready for Lines, No MX required')], default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='acft',
            name='crews_assigned',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='acft.crew'),
        ),
    ]

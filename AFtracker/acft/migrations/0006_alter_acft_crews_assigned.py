# Generated by Django 4.0 on 2023-09-03 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_crew_crew_name'),
        ('acft', '0005_acft_acft_mission_status_alter_acft_acft_mx_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acft',
            name='crews_assigned',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.crew'),
        ),
    ]

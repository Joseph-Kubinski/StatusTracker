# Generated by Django 4.0 on 2023-09-03 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_squadron_workcenter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crew',
            name='work_center',
        ),
        migrations.AddField(
            model_name='crew',
            name='workplace',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.workcenter'),
        ),
    ]

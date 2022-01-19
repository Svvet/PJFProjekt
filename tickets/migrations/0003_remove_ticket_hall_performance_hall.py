# Generated by Django 4.0.1 on 2022-01-18 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_hall_alter_ticket_hall'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='hall',
        ),
        migrations.AddField(
            model_name='performance',
            name='hall',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tickets.hall'),
        ),
    ]

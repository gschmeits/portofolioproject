# Generated by Django 2.1.3 on 2019-03-05 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesis', '0002_auto_20190305_1952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issues',
            old_name='thes',
            new_name='thesnr',
        ),
        migrations.AlterField(
            model_name='issues',
            name='status',
            field=models.CharField(choices=[(1, 'To Do'), (2, 'In Progress'), (3, 'Code Review'), (4, 'Redo'), (5, 'Test'), (6, 'Done')], default=1, max_length=20),
        ),
    ]

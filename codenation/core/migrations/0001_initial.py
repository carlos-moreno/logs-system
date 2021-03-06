# Generated by Django 3.0.8 on 2020-07-11 00:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('status', models.BooleanField(default=True, verbose_name='status')),
                ('environment', models.CharField(choices=[('PRODUCTION', 'PRODUCTION'), ('HOMOLOGATION', 'HOMOLOGATION'), ('DEVELOPMENT', 'DEVELOPMENT')], max_length=15, verbose_name='environment')),
                ('version', models.CharField(max_length=5, verbose_name='version')),
                ('address', models.GenericIPAddressField(verbose_name='ip address')),
            ],
            options={
                'db_table': 'agent',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id')),
                ('level', models.CharField(choices=[('CRITICAL', 'CRITICAL'), ('DEBUG', 'DEBUG'), ('ERROR', 'ERROR'), ('WARNING', 'WARNING'), ('INFO', 'INFO')], max_length=20, verbose_name='level')),
                ('message', models.TextField(verbose_name='message')),
                ('shelved', models.BooleanField(default=False, verbose_name='shelved')),
                ('received_in', models.DateField(auto_now_add=True, verbose_name='received in')),
                ('occurrences', models.IntegerField(editable=False, verbose_name='occurrences')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Agent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'event',
            },
        ),
    ]

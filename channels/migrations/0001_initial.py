# Generated by Django 3.2.4 on 2021-06-28 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractItem',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.timestampedmodel')),
                ('name', models.CharField(max_length=80)),
            ],
            bases=('core.timestampedmodel',),
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('abstractitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='channels.abstractitem')),
            ],
            bases=('channels.abstractitem',),
        ),
        migrations.CreateModel(
            name='Resolution',
            fields=[
                ('abstractitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='channels.abstractitem')),
            ],
            bases=('channels.abstractitem',),
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.timestampedmodel')),
                ('name', models.CharField(max_length=140)),
                ('image', models.ImageField(blank=True, null=True, upload_to='channel_photos')),
                ('on_air', models.BooleanField(default=False)),
                ('channel_host', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='channel', to=settings.AUTH_USER_MODEL)),
                ('genre', models.ManyToManyField(blank=True, to='channels.Genre')),
                ('resolution', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='channels.resolution')),
            ],
            bases=('core.timestampedmodel',),
        ),
    ]
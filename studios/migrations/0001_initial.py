# Generated by Django 3.2.4 on 2021-06-28 07:43

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
            name='StudioAbstractItem',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.timestampedmodel')),
                ('name', models.CharField(max_length=80)),
            ],
            bases=('core.timestampedmodel',),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('studioabstractitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='studios.studioabstractitem')),
            ],
            bases=('studios.studioabstractitem',),
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.timestampedmodel')),
                ('name', models.CharField(max_length=200, null=True)),
                ('desc', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='studio_photos')),
                ('studio_host', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('core.timestampedmodel',),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.timestampedmodel')),
                ('title', models.CharField(max_length=200, null=True)),
                ('body', models.TextField(blank=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='studios.post')),
                ('p_studio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='studios.studio')),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('core.timestampedmodel',),
        ),
    ]

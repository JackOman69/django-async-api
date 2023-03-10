# Generated by Django 4.1.4 on 2022-12-22 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=128)),
                ('name', models.CharField(max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RequestBody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Request_id', models.CharField(default='', max_length=128)),
                ('ClubId', models.CharField(default='', max_length=128)),
                ('Method', models.CharField(default='', max_length=128)),
                ('request_body', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='request_body', to='api.sources')),
            ],
        ),
        migrations.CreateModel(
            name='ParametersRequestBody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ServiceId', models.CharField(blank=True, default='', max_length=30)),
                ('Parameters', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Parameters', to='api.requestbody')),
            ],
        ),
        migrations.CreateModel(
            name='BasicAuth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(default='', max_length=30)),
                ('password', models.CharField(default='', max_length=30)),
                ('basic_auth', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='basic_auth', to='api.sources')),
            ],
        ),
    ]

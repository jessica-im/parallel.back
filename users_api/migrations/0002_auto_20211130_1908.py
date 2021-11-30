# Generated by Django 3.2.9 on 2021-11-30 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('image', models.CharField(max_length=1000)),
                ('status', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=1000)),
                ('about', models.CharField(max_length=1000)),
                ('link', models.CharField(max_length=1000)),
                ('github', models.CharField(max_length=1000)),
                ('profile', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='users_api.profile')),
            ],
        ),
        migrations.AddField(
            model_name='useraccount',
            name='profile',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='users_api.profile'),
        ),
    ]
# Generated by Django 3.2 on 2021-05-13 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('readdataapp', '0010_auto_20210513_0411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.TextField(default=1620919788.073841),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.TextField(default=1620919788.0734534),
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followers', models.ManyToManyField(blank=True, null=True, related_name='followers', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='relationship', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
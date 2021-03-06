# Generated by Django 3.0 on 2020-06-25 05:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_name', models.CharField(max_length=50, verbose_name='Наименование уровня')),
                ('level_description', models.TextField(verbose_name='Описание уровня')),
                ('level_pubdate', models.DateTimeField(auto_now=True, verbose_name='Дата публикации')),
                ('level_content', models.TextField(verbose_name='Код уровня')),
            ],
        ),
        migrations.CreateModel(
            name='LevelRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(verbose_name='Рейтинг')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Level')),
            ],
        ),
    ]

# Generated by Django 4.0 on 2023-02-08 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_user_degree_alter_user_about_alter_user_birth_day_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Название')),
                ('degree', models.IntegerField(choices=[(0, 'Безалкогольное'), (1, 'Слабоалкогольное'), (2, 'Крепкое')], verbose_name='Степень алкогольности')),
            ],
            options={
                'verbose_name': 'Напиток',
                'verbose_name_plural': 'Напитки',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Название')),
                ('abbreviation', models.SlugField(max_length=5, verbose_name='Аббревиатура')),
            ],
            options={
                'verbose_name': 'Язык',
                'verbose_name_plural': 'Языки',
                'ordering': ('abbreviation',),
            },
        ),
        migrations.CreateModel(
            name='UserLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.language', verbose_name='Язык')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='languages', to='users.user', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Пользователь + язык',
                'verbose_name_plural': 'Пользователи + языки',
            },
        ),
        migrations.CreateModel(
            name='UserDrink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.drink', verbose_name='Напиток')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drinks', to='users.user', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Пользователь + напиток',
                'verbose_name_plural': 'Пользователи + напитки',
            },
        ),
        migrations.AddField(
            model_name='language',
            name='users',
            field=models.ManyToManyField(through='core.UserLanguage', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь(и)'),
        ),
    ]

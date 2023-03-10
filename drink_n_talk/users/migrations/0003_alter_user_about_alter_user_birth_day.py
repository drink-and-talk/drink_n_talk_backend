# Generated by Django 4.0 on 2023-02-09 14:44

from django.db import migrations, models
import spare.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_degree_alter_user_about_alter_user_birth_day_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='about',
            field=models.TextField(blank=True, max_length=254, verbose_name='О себе'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_day',
            field=models.DateField(validators=[spare.validators.validate_birthday], verbose_name='День рождения'),
        ),
    ]

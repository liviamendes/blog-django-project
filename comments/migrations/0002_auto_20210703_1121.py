# Generated by Django 3.2.5 on 2021-07-03 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_email',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_name',
            field=models.CharField(max_length=150, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_published',
            field=models.BooleanField(default=False, verbose_name='Published'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='User Comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_comment',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date'),
        ),
    ]

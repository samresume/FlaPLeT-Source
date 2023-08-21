# Generated by Django 4.1.5 on 2023-06-03 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solarflare', '0010_remove_project_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='country',
            field=models.CharField(blank=True, choices=[('unitedstates', 'United States'), ('canada', 'Canada')], max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='state',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='type',
            field=models.CharField(blank=True, choices=[('personal', 'Personal'), ('organization', 'Organization'), ('school', 'School')], max_length=32, null=True),
        ),
    ]
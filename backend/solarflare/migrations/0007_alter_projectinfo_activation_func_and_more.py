# Generated by Django 4.1.5 on 2023-05-30 18:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solarflare', '0006_remove_projectinfo_hyperparameter_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectinfo',
            name='activation_func',
            field=models.CharField(blank=True, choices=[('sigmoid', 'Sigmoid'), ('relu', 'ReLU'), ('tanh', 'Tanh')], max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='projectinfo',
            name='data_augmentation',
            field=models.CharField(blank=True, choices=[('pocket', 'Pocket'), ('timegan', 'TimeGan')], max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='projectinfo',
            name='epochs',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='projectinfo',
            name='layers',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='projectinfo',
            name='learning_rate',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)]),
        ),
        migrations.AlterField(
            model_name='projectinfo',
            name='normalize',
            field=models.IntegerField(blank=True, choices=[(1, 'Yes'), (0, 'No')], null=True),
        ),
        migrations.AlterField(
            model_name='projectinfo',
            name='optimization',
            field=models.CharField(blank=True, choices=[('gradientdescent', 'Gradient Descent'), ('adam', 'Adam Optimizer')], max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='projectinfo',
            name='train_split',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(50), django.core.validators.MaxValueValidator(90)]),
        ),
    ]

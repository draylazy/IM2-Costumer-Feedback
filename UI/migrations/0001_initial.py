# Generated by Django 5.1.1 on 2024-10-27 09:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('occupation', models.CharField(blank=True, max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_1', models.IntegerField(blank=True, choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')], null=True)),
                ('question_2', models.IntegerField(blank=True, choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')], null=True)),
                ('question_3', models.IntegerField(blank=True, choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')], null=True)),
                ('question_4', models.IntegerField(blank=True, choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')], null=True)),
                ('question_5', models.IntegerField(blank=True, choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')], null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='UI.customer')),
            ],
        ),
    ]

# Generated by Django 5.1.1 on 2024-10-27 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='question_10',
            field=models.IntegerField(blank=True, choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')], null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='question_6',
            field=models.IntegerField(blank=True, choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')], null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='question_7',
            field=models.IntegerField(blank=True, choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')], null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='question_8',
            field=models.IntegerField(blank=True, choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')], null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='question_9',
            field=models.IntegerField(blank=True, choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')], null=True),
        ),
    ]

# Generated by Django 3.2.4 on 2021-06-08 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_answer_classify_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='collect_ques',
            field=models.ManyToManyField(to='accounts.Question'),
        ),
    ]

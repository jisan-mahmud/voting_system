# Generated by Django 5.1.1 on 2024-09-25 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_vote_voter_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoteCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('total_vote', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 2.2.6 on 2019-10-11 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_auto_20191011_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField()),
                ('text', models.TextField()),
                ('coments', models.ManyToManyField(to='api_users.CommentSkill')),
                ('cv', models.ForeignKey(on_delete=None, to='users.CV')),
                ('profile', models.ForeignKey(on_delete=None, to='users.Profile')),
            ],
        ),
    ]

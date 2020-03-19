# Generated by Django 2.2.3 on 2020-03-15 02:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GameName', models.CharField(default='', max_length=128)),
                ('GameRating', models.IntegerField(default=0)),
                ('GameImage', models.ImageField(blank=True, upload_to='profile_images')),
                ('Gamedescription', models.TextField(max_length=200)),
                ('GameCategory', models.CharField(blank=True, max_length=50)),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GameName', models.CharField(default='', max_length=128)),
                ('GameImage', models.ImageField(blank=True, upload_to='profile_images')),
                ('ReviewerName', models.CharField(max_length=128)),
                ('Review', models.TextField(max_length=200)),
                ('Graphics', models.IntegerField(default=0)),
                ('Storyline', models.IntegerField(default=0)),
                ('Gameplay', models.IntegerField(default=0)),
                ('slug', models.SlugField(blank=True)),
                ('games', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playerhq.Games')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GameName', models.CharField(default='', max_length=128)),
                ('CommentName', models.CharField(max_length=128)),
                ('Comments', models.TextField(blank=True, max_length=200)),
                ('reviews', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playerhq.Reviews')),
            ],
        ),
    ]
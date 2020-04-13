# Generated by Django 2.2 on 2020-04-11 07:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_archived', models.BooleanField(blank=True, default=False)),
                ('is_published', models.BooleanField(blank=True, default=True)),
                ('created_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('modified_date', models.DateTimeField(blank=True, editable=False, null=True)),
                ('title', models.CharField(default='', max_length=150)),
                ('slug', models.SlugField()),
                ('content', models.TextField(default='')),
                ('picture', models.FileField(null=True, upload_to='news')),
                ('picture_thumbnail', models.FileField(null=True, upload_to='news')),
            ],
            options={
                'ordering': ['-created_date'],
                'abstract': False,
            },
        ),
    ]
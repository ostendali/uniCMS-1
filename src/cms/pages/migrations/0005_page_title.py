# Generated by Django 3.1.4 on 2020-12-28 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmspages', '0004_auto_20201227_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='title',
            field=models.CharField(default='titolo pagina', max_length=256),
            preserve_default=False,
        ),
    ]
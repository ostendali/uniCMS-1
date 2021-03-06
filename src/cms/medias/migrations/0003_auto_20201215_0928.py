# Generated by Django 3.1.3 on 2020-12-15 09:28

import cms.medias.models
import cms.medias.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsmedias', '0002_auto_20201210_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='file',
            field=models.FileField(upload_to=cms.medias.models.context_media_path, validators=[cms.medias.validators.validate_file_extension, cms.medias.validators.validate_file_size, cms.medias.validators.validate_image_size_ratio]),
        ),
    ]

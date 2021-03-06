# Generated by Django 3.1.2 on 2020-12-18 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmstemplates', '0004_auto_20201218_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagetemplate',
            name='image',
            field=models.ImageField(blank=True, max_length=512, null=True, upload_to='images/page_templates_previews'),
        ),
        migrations.AddField(
            model_name='templateblock',
            name='image',
            field=models.ImageField(blank=True, max_length=512, null=True, upload_to='images/block_templates_previews'),
        ),
        migrations.AlterField(
            model_name='templateblock',
            name='type',
            field=models.TextField(choices=[('cms.templates.blocks.PublicationContentPlaceholderBlock', 'Publication Content Placeholder'), ('cms.templates.blocks.HtmlBlock', 'HTML Block'), ('cms.templates.blocks.JSONBlock', 'JSON Block')]),
        ),
    ]

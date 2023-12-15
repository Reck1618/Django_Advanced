# Generated by Django 4.2.6 on 2023-12-15 10:50

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_tag_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hero_image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='hero_images'),
        ),
        migrations.AddField(
            model_name='post',
            name='ppoi',
            field=versatileimagefield.fields.PPOIField(blank=True, default='0.5x0.5', editable=False, max_length=20, null=True),
        ),
    ]

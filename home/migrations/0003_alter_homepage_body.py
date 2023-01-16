# Generated by Django 3.2.16 on 2022-12-27 01:02

from django.db import migrations
import wagtail.blocks
import wagtail.contrib.table_block.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20221226_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(template='home/blocks/heading.html')), ('paragraph', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('logo', wagtail.images.blocks.ImageChooserBlock(template='home/blocks/logo.html')), ('date', wagtail.blocks.DateBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='home/blocks/table.html')), ('quote', wagtail.blocks.RichTextBlock(template='home/blocks/quote.html'))], use_json_field=True),
        ),
    ]
# Generated by Django 2.2.2 on 2019-06-17 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('podcasting', '0004_auto_20160822_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='description',
            field=models.TextField(blank=True, help_text="\n            This is your chance to tell potential subscribers all about your podcast.\n            Describe your subject matter, media format, episode schedule, and other\n            relevant info so that they know what they'll be getting when they\n            subscribe. In addition, make a list of the most relevant search terms\n            that you want your podcast to match, then build them into your\n            description. Note that iTunes removes podcasts that include lists of\n            irrelevant words in the itunes:summary, description, or\n            itunes:keywords tags. This field can be up to 4000 plain text characters.\n            No HTML tags or styling allowed.", max_length=4000, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='episode',
            name='original_image',
            field=models.ForeignKey(blank=True, default=None, help_text='\n                A podcast must have 1400 x 1400 pixel cover art in JPG or PNG\n                format using RGB color space. See our technical spec for\n                details. To be eligible for featuring on iTunes Stores,\n                choose an attractive, original, and square JPEG (.jpg) or\n                PNG (.png) image at a size of 1400x1400 pixels. The image\n                will be scaled down to 50x50 pixels at smallest in iTunes.\n                For reference see the <a\n                href="http://www.apple.com/itunes/podcasts/specs.html#metadata">iTunes\n                Podcast specs</a>.<br /><br /> For episode artwork to\n                display in iTunes, image must be <a\n                href="http://answers.yahoo.com/question/index?qid=20080501164348AAjvBvQ">\n                saved to file\'s <strong>metadata</strong></a> before\n                enclosure uploading!', null=True, on_delete=django.db.models.deletion.PROTECT, to='photologue.Photo', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='show',
            name='license',
            field=models.CharField(help_text='To publish a podcast to iTunes it is required to set a license type.', max_length=255, verbose_name='license'),
        ),
        migrations.AlterField(
            model_name='show',
            name='original_image',
            field=models.ForeignKey(blank=True, default=None, help_text='\n                A podcast must have 1400 x 1400 pixel cover art in JPG or PNG\n                format using RGB color space. See our technical spec for\n                details. To be eligible for featuring on iTunes Stores,\n                choose an attractive, original, and square JPEG (.jpg) or\n                PNG (.png) image at a size of 1400x1400 pixels. The image\n                will be scaled down to 50x50 pixels at smallest in iTunes.\n                For reference see the <a\n                href="http://www.apple.com/itunes/podcasts/specs.html#metadata">iTunes\n                Podcast specs</a>.<br /><br /> For episode artwork to\n                display in iTunes, image must be <a\n                href="http://answers.yahoo.com/question/index?qid=20080501164348AAjvBvQ">\n                saved to file\'s <strong>metadata</strong></a> before\n                enclosure uploading!', null=True, on_delete=django.db.models.deletion.SET_NULL, to='photologue.Photo', verbose_name='image'),
        ),
    ]

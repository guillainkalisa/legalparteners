from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='photo_focus_x',
            field=models.PositiveIntegerField(default=50),
        ),
        migrations.AddField(
            model_name='teammember',
            name='photo_focus_y',
            field=models.PositiveIntegerField(default=50),
        ),
    ]

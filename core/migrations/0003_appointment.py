# Generated migration for Appointment model

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_teammember_photo_focus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Your full name', max_length=150)),
                ('email', models.EmailField(help_text='Your email address', max_length=254)),
                ('message', models.TextField(blank=True, help_text='Additional notes or details about your inquiry')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('consultant', models.ForeignKey(blank=True, help_text='Leave blank to auto-assign', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.teammember')),
            ],
            options={
                'verbose_name': 'Appointment',
                'verbose_name_plural': 'Appointments',
                'ordering': ['-created_at'],
            },
        ),
    ]

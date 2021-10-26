# Generated by Django 2.2.4 on 2021-09-28 11:20

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import website.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CFP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('date_of_announcement', models.DateTimeField(blank=True, null=True)),
                ('receive_proposals', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_author1', models.CharField(default='None', max_length=200)),
                ('name_of_author2', models.CharField(default='None', max_length=200)),
                ('about_the_authors', models.TextField(max_length=500)),
                ('email', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=250)),
                ('abstract', models.TextField(max_length=700)),
                ('prerequisite', models.CharField(max_length=750)),
                ('duration', models.CharField(max_length=100)),
                ('attachment', models.FileField(upload_to=website.models.get_document_dir)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default='Pending', max_length=100)),
                ('proposal_type', models.CharField(max_length=100)),
                ('tags', models.CharField(max_length=250)),
                ('open_to_share', models.CharField(default=1, max_length=2)),
                ('terms_and_conditions', models.BooleanField(default='True')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_type', models.TextField(blank=True, max_length=500, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('registration_ticket', models.CharField(blank=True, max_length=100, null=True)),
                ('registration_description', models.TextField(blank=True, max_length=500, null=True)),
                ('display_registration_type', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TentativeSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_table', models.TextField(blank=True, null=True)),
                ('display_schedule_table', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=700)),
                ('proposal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Proposal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, choices=[('Mr', 'Mr.'), ('Miss', 'Ms.'), ('Professor', 'Prof.'), ('Doctor', 'Dr.')], max_length=32)),
                ('institute', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be entered                                 in the format: '9999999999'.                                Up to 10 digits allowed.", regex='^.{10}$')])),
                ('position', models.CharField(choices=[('student', 'Student'), ('faculty', 'Faculty'), ('industry_people', 'Industry People')], default='student', help_text='Selected catagoery ID shold be required', max_length=32)),
                ('how_did_you_hear_about_us', models.CharField(blank=True, choices=[('Poster', 'Poster'), ('FOSSEE website', 'FOSSEE website'), ('Google', 'Google'), ('Social Media', 'Social Media'), ('From other College', 'From other College')], max_length=255)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('activation_key', models.CharField(blank=True, max_length=255, null=True)),
                ('key_expiry_time', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=700)),
                ('proposal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Proposal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 2.2.8 on 2021-09-22 22:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models
import user_profiles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferred_name', models.CharField(blank=True, db_index=True, help_text='What would you like us to call you?', max_length=64)),
                ('middle_name', models.CharField(blank=True, max_length=64)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('F', 'Female'), ('M', 'Male')], max_length=1)),
                ('picture', models.ImageField(blank=True, null=True, upload_to=user_profiles.models.UserProfile.rename_file)),
                ('alt_email', models.EmailField(blank=True, help_text='Preferably at least one of your email addresses on record will be a non-edu address (e.g., @gmail.com, @yahoo.com).', max_length=254, verbose_name='Alternate email address')),
                ('cell_phone', localflavor.us.models.PhoneNumberField(blank=True, max_length=20)),
                ('home_phone', localflavor.us.models.PhoneNumberField(blank=True, max_length=20)),
                ('receive_text', models.BooleanField(default=False, help_text='Can you send and receive text messages on your cell phone?')),
                ('local_address1', models.CharField(blank=True, max_length=256, verbose_name='Local Address Line 1')),
                ('local_address2', models.CharField(blank=True, max_length=256, verbose_name='Local Address Line 2')),
                ('local_city', models.CharField(blank=True, max_length=128)),
                ('local_state', localflavor.us.models.USStateField(blank=True, choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], max_length=2)),
                ('local_zip', models.CharField(blank=True, max_length=10, verbose_name='Local ZIP')),
                ('perm_address1', models.CharField(blank=True, help_text='Either a permanent or an international address is required.', max_length=256, verbose_name='Permanent Address Line 1')),
                ('perm_address2', models.CharField(blank=True, max_length=256, verbose_name='Permanent Address Line 2')),
                ('perm_city', models.CharField(blank=True, max_length=128, verbose_name='Permanent City')),
                ('perm_state', localflavor.us.models.USStateField(blank=True, choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], default='CA', max_length=2, verbose_name='Permanent State')),
                ('perm_zip', models.CharField(blank=True, max_length=10, verbose_name='Permanent ZIP')),
                ('international_address', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('alt_officer_email', models.EmailField(blank=True, help_text='Set an alternate email on the Officers page. Don\'t include the domain name (".edu" or ".com") if obvious (to mitigate email scrapers). Leave blank to keep default tbp email (for officers only).', max_length=254, verbose_name='Alternate officer email address', default='')),
            ],
            options={
                'ordering': ('preferred_name', 'user__last_name'),
            },
        ),
        migrations.CreateModel(
            name='StudentOrgUserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True)),
                ('initiation_term', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.Term', verbose_name='Term initiated into the organization.')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Student Organization User Profile',
                'ordering': ('user',),
            },
        ),
        migrations.CreateModel(
            name='CollegeStudentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_code', models.CharField(blank=True, max_length=20)),
                ('grad_term', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.Term', verbose_name='Graduation term')),
                ('major', models.ManyToManyField(to='base.Major')),
                ('start_term', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.Term', verbose_name='First term at this school')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'college student info',
            },
        ),
    ]

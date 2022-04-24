# Generated by Django 4.0.3 on 2022-04-23 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0003_rename_created_profile_time_created_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgressState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='RawData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=120, null=True)),
                ('file_obj', models.FileField(null=True, upload_to='metadata')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScienceKeyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=120)),
                ('term', models.CharField(max_length=120)),
                ('variable1', models.CharField(blank=True, max_length=120, null=True)),
                ('variable2', models.CharField(blank=True, max_length=120, null=True)),
                ('variable3', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_updated', models.DateTimeField(auto_now=True)),
                ('metadata_id', models.CharField(editable=False, max_length=12, unique=True)),
                ('metadata_name', models.CharField(max_length=120)),
                ('aas_project_number', models.CharField(blank=True, max_length=12, null=True)),
                ('parent_metadata_id', models.CharField(blank=True, max_length=12, null=True)),
                ('summary', models.TextField(blank=True, default='...', null=True)),
                ('purpose', models.TextField(blank=True, default='...', null=True)),
                ('quality', models.TextField(blank=True, default='...', null=True)),
                ('use_constraints', models.TextField(blank=True, default='...', null=True)),
                ('access_constraints', models.TextField(blank=True, default='...', null=True)),
                ('references', models.TextField(blank=True, null=True)),
                ('first_name', models.CharField(blank=True, max_length=120, null=True)),
                ('last_name', models.CharField(blank=True, max_length=120, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('additional_keywords', models.TextField(blank=True, null=True)),
                ('instrument', models.CharField(blank=True, max_length=120, null=True)),
                ('platform', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
                ('dataset_progress', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='metadata.progressstate')),
                ('rawdata', models.ManyToManyField(to='metadata.rawdata')),
                ('science_keywords', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='metadata.sciencekeyword')),
            ],
            options={
                'ordering': ('-time_created',),
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('keywords', models.ManyToManyField(to='metadata.sciencekeyword')),
            ],
        ),
    ]
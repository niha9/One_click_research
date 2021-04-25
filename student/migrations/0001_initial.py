# Generated by Django 2.1.7 on 2019-03-03 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Std_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_designation', models.CharField(max_length=100)),
                ('st_any_pub', models.TextField(default='banda')),
                ('st_study_purpose', models.CharField(choices=[('D', 'DNB'), ('M', 'MSc'), ('P', 'PhD'), ('O', 'Others')], max_length=100)),
                ('st_study_other', models.CharField(max_length=100)),
                ('status_choice_id', models.IntegerField(choices=[(1, 'Not applied'), (2, 'applied'), (3, 'approved'), (4, 'rejected')], default=1)),
                ('st_project_status', models.IntegerField(choices=[(0, 'Not Filled'), (1, 'Guide Approval Pending'), (2, 'Sectretary Approval Pending '), (3, 'Director Approval Pending'), (4, 'IRB Review Pending'), (5, 'Final Review Pending'), (6, 'Student queryset'), (7, 'Guide Forward for IRB'), (8, 'Secretary Forward for IRB'), (9, 'Final Review Complete')], default=0)),
                ('is_initreview_done', models.BooleanField(default=False)),
                ('is_interreview_done', models.BooleanField(default=False)),
                ('is_finalreview_done', models.BooleanField(default=False)),
            ],
        ),
    ]

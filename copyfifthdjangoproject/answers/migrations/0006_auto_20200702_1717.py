# Generated by Django 3.0.4 on 2020-07-02 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0018_auto_20200702_1717'),
        ('users', '0005_remove_studentprofile_marks'),
        ('answers', '0005_auto_20200627_1807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='marks',
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scored', models.IntegerField(default=0)),
                ('OutOf', models.IntegerField(default=10)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.Activity')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='answers.Answer')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.StudentProfile')),
            ],
        ),
    ]
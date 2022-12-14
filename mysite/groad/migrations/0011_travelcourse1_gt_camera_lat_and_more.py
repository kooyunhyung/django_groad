# Generated by Django 4.0.6 on 2022-11-06 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groad', '0010_rename_gt1_seq_travelcourse3_gt_seq_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='travelcourse1',
            name='gt_camera_lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse1',
            name='gt_camera_lng',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse1',
            name='gt_course_Id1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse1',
            name='gt_course_Id2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse1',
            name='gt_course_Id3',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse1',
            name='gt_course_Id4',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse1',
            name='gt_course_Id5',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse1',
            name='gt_course_key',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse1',
            name='gt_course_lat1',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse1',
            name='gt_course_lat2',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse1',
            name='gt_course_lat3',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse1',
            name='gt_course_lat4',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse1',
            name='gt_course_lat5',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse1',
            name='gt_course_lng1',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse1',
            name='gt_course_lng2',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse1',
            name='gt_course_lng3',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse1',
            name='gt_course_lng4',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse1',
            name='gt_course_lng5',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse1',
            name='gt_course_name1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse1',
            name='gt_course_name2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse1',
            name='gt_course_name3',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse1',
            name='gt_course_name4',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse1',
            name='gt_course_name5',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse1',
            name='gt_course_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse1',
            name='gt_distance',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse1',
            name='gt_time',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse1',
            name='gt_zoom',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse2',
            name='gt_camera_lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse2',
            name='gt_camera_lng',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse2',
            name='gt_course_Id1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse2',
            name='gt_course_Id2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse2',
            name='gt_course_Id3',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse2',
            name='gt_course_Id4',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse2',
            name='gt_course_Id5',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse2',
            name='gt_course_key',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse2',
            name='gt_course_lat1',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse2',
            name='gt_course_lat2',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse2',
            name='gt_course_lat3',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse2',
            name='gt_course_lat4',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse2',
            name='gt_course_lat5',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse2',
            name='gt_course_lng1',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse2',
            name='gt_course_lng2',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse2',
            name='gt_course_lng3',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse2',
            name='gt_course_lng4',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse2',
            name='gt_course_lng5',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse2',
            name='gt_course_name1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse2',
            name='gt_course_name2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse2',
            name='gt_course_name3',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse2',
            name='gt_course_name4',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse2',
            name='gt_course_name5',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse2',
            name='gt_course_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse2',
            name='gt_distance',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse2',
            name='gt_time',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse2',
            name='gt_zoom',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse3',
            name='gt_camera_lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse3',
            name='gt_camera_lng',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse3',
            name='gt_course_Id1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse3',
            name='gt_course_Id2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse3',
            name='gt_course_Id3',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse3',
            name='gt_course_Id4',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse3',
            name='gt_course_Id5',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse3',
            name='gt_course_key',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse3',
            name='gt_course_lat1',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse3',
            name='gt_course_lat2',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse3',
            name='gt_course_lat3',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse3',
            name='gt_course_lat4',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse3',
            name='gt_course_lat5',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse3',
            name='gt_course_lng1',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse3',
            name='gt_course_lng2',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse3',
            name='gt_course_lng3',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse3',
            name='gt_course_lng4',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse3',
            name='gt_course_lng5',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse3',
            name='gt_course_name1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse3',
            name='gt_course_name2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse3',
            name='gt_course_name3',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse3',
            name='gt_course_name4',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse3',
            name='gt_course_name5',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse3',
            name='gt_course_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse3',
            name='gt_distance',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse3',
            name='gt_time',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse3',
            name='gt_zoom',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse4',
            name='gt_camera_lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse4',
            name='gt_camera_lng',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse4',
            name='gt_course_Id1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse4',
            name='gt_course_Id2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse4',
            name='gt_course_Id3',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse4',
            name='gt_course_Id4',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse4',
            name='gt_course_Id5',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse4',
            name='gt_course_key',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse4',
            name='gt_course_lat1',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse4',
            name='gt_course_lat2',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse4',
            name='gt_course_lat3',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse4',
            name='gt_course_lat4',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse4',
            name='gt_course_lat5',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse4',
            name='gt_course_lng1',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse4',
            name='gt_course_lng2',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse4',
            name='gt_course_lng3',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse4',
            name='gt_course_lng4',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse4',
            name='gt_course_lng5',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse4',
            name='gt_course_name1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse4',
            name='gt_course_name2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse4',
            name='gt_course_name3',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse4',
            name='gt_course_name4',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse4',
            name='gt_course_name5',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse4',
            name='gt_course_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse4',
            name='gt_distance',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='travelcourse4',
            name='gt_time',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='travelcourse4',
            name='gt_zoom',
            field=models.FloatField(null=True),
        ),
    ]

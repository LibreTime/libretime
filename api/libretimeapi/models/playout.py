from django.db import models

from .files import File


class ListenerCount(models.Model):
    timestamp = models.ForeignKey("Timestamp", models.DO_NOTHING)
    mount_name = models.ForeignKey("MountName", models.DO_NOTHING)
    listener_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = "cc_listener_count"


class LiveLog(models.Model):
    state = models.CharField(max_length=32)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "cc_live_log"


class PlayoutHistory(models.Model):
    file = models.ForeignKey(File, models.DO_NOTHING, blank=True, null=True)
    starts = models.DateTimeField()
    ends = models.DateTimeField(blank=True, null=True)
    instance = models.ForeignKey(
        "ShowInstance", models.DO_NOTHING, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "cc_playout_history"


class PlayoutHistoryMetadata(models.Model):
    history = models.ForeignKey(PlayoutHistory, models.DO_NOTHING)
    key = models.CharField(max_length=128)
    value = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = "cc_playout_history_metadata"


class PlayoutHistoryTemplate(models.Model):
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = "cc_playout_history_template"


class PlayoutHistoryTemplateField(models.Model):
    template = models.ForeignKey(PlayoutHistoryTemplate, models.DO_NOTHING)
    name = models.CharField(max_length=128)
    label = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    is_file_md = models.BooleanField()
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = "cc_playout_history_template_field"


class Timestamp(models.Model):
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "cc_timestamp"

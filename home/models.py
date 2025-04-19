from django.db import models

class Draftee(models.Model):
    id = models.AutoField(primary_key=True)
    month = models.IntegerField()
    day = models.IntegerField()
    birthyear = models.CharField(max_length=50)
    drawyear = models.IntegerField()
    draftyear = models.IntegerField()
    halfyear = models.CharField(max_length=50)
    draftnumber = models.IntegerField()

    class Meta:
        db_table = 'draft_info'
        managed = False

class Admin(models.Model):
    draftyear = models.IntegerField(primary_key=True)
    drawdate = models.CharField(max_length=50)
    birthyear = models.CharField(max_length=50)
    maxcalled = models.IntegerField()

    class Meta:
        db_table = 'draft_admin'
        managed = False
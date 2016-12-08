# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Commentinfo(models.Model):
    commentuuid = models.CharField(db_column='commentUUID', primary_key=True, max_length=100)  # Field name made lowercase.
    postuuid = models.CharField(db_column='postUUID', unique=True, max_length=100)  # Field name made lowercase.
    useruuid = models.CharField(db_column='userUUID', max_length=100)  # Field name made lowercase.
    commenttext = models.TextField()
    commentdate = models.TextField()

    class Meta:
        managed = False
        db_table = 'commentinfo'


class Postinfo(models.Model):
    postuuid = models.CharField(db_column='postUUID', primary_key=True, max_length=100)  # Field name made lowercase.
    useruuid = models.CharField(db_column='userUUID', unique=True, max_length=45)  # Field name made lowercase.
    title = models.CharField(max_length=100)
    content = models.TextField()
    pubdate = models.TextField()

    class Meta:
        managed = False
        db_table = 'postinfo'


class Userinfo(models.Model):
    useruuid = models.CharField(db_column='userUUID', primary_key=True, max_length=100)  # Field name made lowercase.
    username = models.CharField(unique=True, max_length=45)
    passworld = models.CharField(max_length=45)
    email = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userinfo'

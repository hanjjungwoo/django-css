from django.db import models

# Create your models here.


# React for Django
class Product(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class AllCity(models.Model):
    index = models.IntegerField(primary_key=True)
    nature = models.FloatField(blank=True, null=True)
    culture = models.FloatField(blank=True, null=True)
    traffic = models.FloatField(blank=True, null=True)
    sleep = models.FloatField(blank=True, null=True)
    food = models.FloatField(blank=True, null=True)
    shopping = models.FloatField(blank=True, null=True)
    inform = models.FloatField(blank=True, null=True)
    conv = models.FloatField(blank=True, null=True)
    kind = models.FloatField(blank=True, null=True)
    activ = models.FloatField(blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    busy = models.FloatField(blank=True, null=True)
    avg = models.FloatField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    cluster = models.IntegerField(db_column='Cluster', blank=True,
                                  null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'all_city'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'), )


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'), )


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'), )


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'), )


class Citydata(models.Model):
    index = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citydata'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType',
                                     models.DO_NOTHING,
                                     blank=True,
                                     null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'), )


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class RefinedData(models.Model):
    index = models.IntegerField(primary_key=True)
    id = models.CharField(max_length=255, blank=True, null=True)
    avg = models.FloatField(blank=True, null=True)
    nature = models.FloatField(blank=True, null=True)
    culture = models.FloatField(blank=True, null=True)
    traffic = models.FloatField(blank=True, null=True)
    sleep = models.FloatField(blank=True, null=True)
    food = models.FloatField(blank=True, null=True)
    shooping = models.FloatField(blank=True, null=True)
    inform = models.FloatField(blank=True, null=True)
    conv = models.FloatField(blank=True, null=True)
    kind = models.FloatField(blank=True, null=True)
    activ = models.FloatField(blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    busy = models.FloatField(blank=True, null=True)
    re = models.FloatField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'refined_data'


class RepresentativeCluster(models.Model):
    index = models.IntegerField(primary_key=True)
    nature = models.FloatField(blank=True, null=True)
    culture = models.FloatField(blank=True, null=True)
    traffic = models.FloatField(blank=True, null=True)
    sleep = models.FloatField(blank=True, null=True)
    food = models.FloatField(blank=True, null=True)
    shopping = models.FloatField(blank=True, null=True)
    inform = models.FloatField(blank=True, null=True)
    conv = models.FloatField(blank=True, null=True)
    kind = models.FloatField(blank=True, null=True)
    activ = models.FloatField(blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    busy = models.FloatField(blank=True, null=True)
    avg = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'representative_cluster'


# class User(models.Model): #???????????? ???????????? models.Model??? ?????????????????????.
#     username = models.CharField(max_length=64,verbose_name = '????????????')
#     password = models.CharField(max_length=64,verbose_name = '????????????')
#     registered_dttm = models.DateTimeField(auto_now_add=True,verbose_name='????????????')
#     #???????????? ????????? ????????? ???????????? ???????????????.

#     def __str__(self): # ??? ?????? ??????
#         return self.username  # User object ?????? ????????? ??????

#     class Meta: #?????? ???????????? ???????????? ???????????? ??????
#         db_table = 'register'
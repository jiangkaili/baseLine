from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class CheckInfo(models.Model):
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')
    username = models.CharField(max_length=11, unique=True, verbose_name='姓名')
    id_card = models.CharField(max_length=54, unique=True, verbose_name='身份证号')

    class Meta:
        db_table = 'tb_check_info'
        verbose_name = '检查信息'
        verbose_name_plural = verbose_name

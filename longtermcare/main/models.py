from django.db import models

# Create your models here.
class employee(models.Model):
    name = models.CharField('성함', max_length=30, blank=False , null=False)
    phone = models.CharField('연락처',max_length=30, blank=False , null=False)
    address = models.TextField('주소', blank=False , null=False)
    preferTime = models.TextField('선호시간', blank=False , null=False)
    created_at = models.DateTimeField(auto_now = True)
    

# Create your models here.

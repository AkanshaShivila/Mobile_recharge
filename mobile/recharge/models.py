from django.db import models
import shortuuid

def tns():

    s = shortuuid.ShortUUID(alphabet="0123456789uabcdefghijklmnopqrstvwxyz")

    otp = s.random(length=15)

    return otp


class Person(models.Model):
    mobile_no = models.CharField(max_length=50)
    operator = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    amount = models.IntegerField(default=1)
    transaction = models.CharField(max_length=15,default=tns)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.mobile_no

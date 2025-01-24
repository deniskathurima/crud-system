from django.db import models

class Member(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    second_name = models.CharField(max_length=100, blank=False, null=False)
    id_no = models.CharField(max_length=100, blank=False, null=False)
    mobile_no = models.CharField(max_length=100, blank=False, null=False)
    date_of_birth = models.CharField(max_length=100, blank=False, null=False)

def __str__(self):
    return self.first_name
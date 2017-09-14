from django.db import models
from django.contrib.auth.models import User

class Url(models.Model):
    address = models.CharField(max_length=50,default="0")
    submitter = models.ForeignKey(User,on_delete=models.CASCADE)
    visit_counter = models.CharField(max_length=20,default="0")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

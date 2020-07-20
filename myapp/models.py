from django.db import models
from datetime import datetime, date, time

# Create your models here.

class Admin(models.Model):
    User_type_Choices = (
        ('Admin','Admin'),
        ('Product Manager','Product Manager'),
    )
    Gender_Choices = (
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others'),
    )
    User_type = models.CharField(max_length=100,null=True,choices=User_type_Choices)
    Username = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100,choices=Gender_Choices)
    Mobile_no = models.IntegerField()
    Emailid = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)

    def __str__(self):
        return self.Username

class Master(models.Model):
    Product_id    = models.AutoField(primary_key=True) 
    Product_name  = models.CharField(max_length = 100)

    def __str__(self):
        template = '{0.Product_name} {0.Product_id}'
        return template.format(self)

class Details(models.Model):
    Product_name_details  = models.ForeignKey(Master,on_delete=models.CASCADE)
    Product_price = models.IntegerField()
    Product_image = models.ImageField(default="image/default.jpg",blank=True,null=False,upload_to='image/')
    Product_model = models.CharField(max_length=100)
    Product_ram   = models.IntegerField()
    Product_detail = models.CharField(max_length=200,null=True)

    def __str__(self):
        template = '{0.Product_name_details.Product_name}'
        return template.format(self)

class Reviews(models.Model):
    User_details  = models.ForeignKey(Admin,on_delete=models.CASCADE)
    Prod_details  = models.ForeignKey(Details,on_delete=models.CASCADE)
    R_created_at = models.DateTimeField(auto_now_add=True, null=True)
    R_updated_at = models.DateTimeField(auto_now=True, null=True)
    User_reviews = models.CharField(max_length=100)
    def __str__(self):
        template = '{0.User_details.Username}'
        return template.format(self)

class Sub_Reviews(models.Model):
    Rply_user_details  = models.ForeignKey(Admin,on_delete=models.CASCADE)
    Reviews_replies  = models.ForeignKey(Reviews,on_delete=models.CASCADE)
    S_R_created_at = models.DateTimeField(auto_now_add=True, null=True)
    S_R_updated_at = models.DateTimeField(auto_now=True, null=True)
    User_replies = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Sub_Reviews (Reviewer, Replier)'

    def __str__(self):
        template = '{0.Reviews_replies.User_details.Username} , {0.Rply_user_details.Username}'
        return template.format(self)

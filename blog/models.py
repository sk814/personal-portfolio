from django.db import models

class Blog_Model(models.Model):
    title=models.CharField(max_length=100,blank=True,default="foobar")
    image=models.ImageField(upload_to="media/blog/images",blank=True)
    url=models.URLField(blank=True)


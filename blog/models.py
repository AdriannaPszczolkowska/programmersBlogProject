from django.db import models

# Create your models here.
# title, text, create Date
class Post(models.Model):
    postId = models.AutoField
    title = models.CharField(max_length = 200)
    text = models.TextField()
    createDate = models.DateField(auto_now_add =True)
    #image = models.ImageField(upload_to ='imagies/', blank =True)

    def __str__(self):
        return self.title + " " + str(self.createDate)
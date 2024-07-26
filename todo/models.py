from django.db import models

class Post(models.Model):
    title=models.CharField('タイトル',max_length=50)
    text=models.TextField('本文',max_length=150)
    image=models.ImageField('画像',upload_to='media/images')
    good=models.IntegerField('いいね',null=True,blank=True,default=0)
    read=models.IntegerField('閲覧数',null=True,blank=True,default=0)
    usertext=models.CharField('紐付け',null=True,blank=True,default='a',max_length=50)
    
    def __str__(self):
        return self.title
from django.db import models

PRIORITY=(('danger','high'),('info','normal'),('success','low'))
class Post(models.Model):
    title=models.CharField('タイトル',max_length=50)
    text=models.TextField('本文',max_length=150)
    image=models.ImageField('画像',upload_to='media/images',null=True, blank=True)
    good=models.IntegerField('いいね',null=True,blank=True,default=0)
    read=models.IntegerField('閲覧数',null=True,blank=True,default=0)
    usertext=models.CharField('紐付け',null=True,blank=True,default='a',max_length=50)
    #追記
    duedate=models.DateTimeField('期限',null=True,blank=True)
    priority=models.CharField(
        '優先度',
        choices=PRIORITY,
        max_length=50,
        null=True
    )
    
    def __str__(self):
        return self.title
from django.db import models

class Post(models.Model):
  title = models.CharField('제목', max_length= 20)
  content = models.CharField('내용', max_length=20)
  region = models.CharField('지역', max_length=20)
  user = models.CharField('작성자', max_length=20)  
  price = models.IntegerField('가격', default=1000)
  photo = models.ImageField('사진', upload_to='posts/%Y%m%d', blank=True)

  created_date = models.DateTimeField('작성일', blank=True, auto_created=True, auto_now_add=True)
  updated_date = models.DateTimeField('수정일', blank=True, auto_created=True, auto_now=True)
from django.db import models

# Create your models here.
#1年
class Topic_1_1(models.Model):
    title = models.CharField(max_length=100, blank=False, null=True)
    
    def __str__(self):
        return self.title

class Topic_1_2(models.Model):
    title = models.CharField(max_length=100, blank=False, null=True)
    
    def __str__(self):
        return self.title
#2年
class Topic_1_3(models.Model):
    title = models.CharField(max_length=100, blank=False, null=True)
    
    def __str__(self):
        return self.title
    
class Topic_1_4(models.Model):
    title = models.CharField(max_length=100, blank=False, null=True)
    
    def __str__(self):
        return self.title
#3年
class Topic_1_5(models.Model):
    title = models.CharField(max_length=100, blank=False, null=True)
    
    def __str__(self):
        return self.title

class Topic_1_6(models.Model):
    title = models.CharField(max_length=100, blank=False, null=True)
    
    def __str__(self):
        return self.title

#編集1年
class Class_1_1(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField('')
    target = models.ForeignKey(Topic_1_1, on_delete=models.CASCADE, verbose_name="対象科目")
    year = models.IntegerField('',blank=False,null=True)
    
    def __str__(self):
        return self.name

class Class_1_2(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField('')
    target = models.ForeignKey(Topic_1_2, on_delete=models.CASCADE, verbose_name="対象科目")
    year = models.IntegerField('',blank=False,null=True)
    
    def __str__(self):
        return self.name
    
#編集2年
class Class_1_3(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField('')
    target = models.ForeignKey(Topic_1_3, on_delete=models.CASCADE, verbose_name="対象科目")
    year = models.IntegerField('',blank=False,null=True)
    
    def __str__(self):
        return self.name
    
class Class_1_4(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField('')
    target = models.ForeignKey(Topic_1_4, on_delete=models.CASCADE, verbose_name="対象科目")
    year = models.IntegerField('',blank=False,null=True)
    
    def __str__(self):
        return self.name
    
#編集3年
class Class_1_5(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField('')
    target = models.ForeignKey(Topic_1_5, on_delete=models.CASCADE, verbose_name="対象科目")
    year = models.IntegerField('',blank=False,null=True)
    
    def __str__(self):
        return self.name
    
class Class_1_6(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField('')
    target = models.ForeignKey(Topic_1_6, on_delete=models.CASCADE, verbose_name="対象科目")
    year = models.IntegerField('',blank=False,null=True)
    
    def __str__(self):
        return self.name
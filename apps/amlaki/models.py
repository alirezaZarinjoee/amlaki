from django.db import models
import utils
# Create your models here.
class Room(models.Model):
    number_of_home=models.PositiveIntegerField(verbose_name='تعداد اتاق')

    def __str__(self):
        return str(self.number_of_home)
    
    class Meta:
        verbose_name='اتاق'
        verbose_name_plural='اتاق ها'


#-----------------------------------------------

class Area(models.Model):
    area=models.TextField(verbose_name='منطقه و محله ملک')

    def __str__(self):
        return self.area
    
    class Meta:
        verbose_name='منطقه'
        verbose_name_plural='منطقه ها'


#-----------------------------------------------
class Metr(models.Model):
    metrazh=models.CharField(verbose_name='رنج متراژ',max_length=100)

    def __str__(self):
        return str(self.metrazh)
    
    class Meta:
        verbose_name='متر'
        verbose_name_plural='متراژ'

#-----------------------------------------------
class TypeHouse(models.Model):
    type_house=models.CharField(verbose_name='نوع ملک', max_length=100)

    def __str__(self):
        return self.type_house
    
    class Meta:
        verbose_name='نوع ملک'
        verbose_name_plural='نوع املاک'
#-----------------------------------------------
class TradeType(models.Model):
    trade_type=models.CharField(verbose_name='نوع معامله ملک', max_length=50)

    def __str__(self):
        return self.trade_type
    
    class Meta:
        verbose_name='نوع معامله'
        verbose_name_plural='نوع معاملات'
        
#-----------------------------------------------
class Floor(models.Model):
    floors=models.PositiveIntegerField(verbose_name='طبقه')

    def __str__(self):
        return str(self.floors)
    
    class Meta:
        verbose_name='طبقه'
        verbose_name_plural='طبقه ها'


#-----------------------------------------------
class Price(models.Model):
    price=models.CharField(null=True,blank=True, max_length=50)

    def __str__(self):
        return str(self.price)
    
    class Meta:
        verbose_name='قیمت'
        verbose_name_plural='قیمت ها'

#-----------------------------------------------
class Melk(models.Model):
    full_name_seller=models.CharField(verbose_name='نام فروشنده', max_length=200,null=True)
    phone_number=models.CharField(verbose_name='شماره تلفن فروشنده' ,max_length=11,null=True)
    is_active=models.BooleanField(verbose_name='فعال/غیرفعال')
    descriptions=models.TextField(verbose_name='توضیحات')
    slug=models.SlugField(null=True,blank=True)
    image_upload=utils.FileUpload('images','melk')
    image=models.ImageField(upload_to=image_upload.upload_to,null=True,blank=True)
    price=models.ForeignKey(Price,null=True,blank=True, on_delete=models.CASCADE)
    floor=models.ForeignKey(Floor, verbose_name='طبقه', on_delete=models.CASCADE,null=True,blank=True)
    trade_type=models.ForeignKey(TradeType, verbose_name='نوع معامله', on_delete=models.CASCADE,null=True,blank=True)
    type_house=models.ForeignKey(TypeHouse, verbose_name='نوع ملک', on_delete=models.CASCADE,null=True,blank=True)
    metr=models.ForeignKey(Metr, verbose_name='متراژ', on_delete=models.CASCADE,null=True,blank=True)
    area=models.ForeignKey(Area, verbose_name='منطقه/محله', on_delete=models.CASCADE,null=True,blank=True)
    room=models.ForeignKey(Room, verbose_name='اتاق', on_delete=models.CASCADE,null=True,blank=True)



    def __str__(self):
        return f'{self.full_name_seller}'
    
    class Meta:
        verbose_name='ملک'
        verbose_name_plural='املاک'

#-----------------------------------------------

class Gallery(models.Model):
    melk=models.ForeignKey(Melk, on_delete=models.CASCADE)
    image_upload=utils.FileUpload('images','gallery')
    image=models.ImageField(upload_to=image_upload.upload_to)


    class Meta:
        verbose_name='تصویر'
        verbose_name_plural='تصاویر'

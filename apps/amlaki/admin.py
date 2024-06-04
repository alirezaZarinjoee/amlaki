from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display=('melk','image')
    list_filter=('melk',)
    search_fields=('melk',)


@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    list_display=('floors',)


@admin.register(TradeType)
class TradeTypeAdmin(admin.ModelAdmin):
    list_display=('trade_type',)


@admin.register(TypeHouse)
class TypeHouseAdmin(admin.ModelAdmin):
    list_display=('type_house',)


@admin.register(Metr)
class MetrAdmin(admin.ModelAdmin):
    list_display=('metrazh',)


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display=('area',)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display=('number_of_home',)




@admin.register(Melk)
class MelkAdmin(admin.ModelAdmin):
    list_display=('full_name_seller','is_active','image','floor','trade_type','type_house','metr','area','room','price')
    list_filter=('is_active','floor','trade_type','type_house','metr','area','room')
    search_fields=('floor','trade_type','type_house','metr','area','room')
    list_editable=['is_active']


    
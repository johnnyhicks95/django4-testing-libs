from django.contrib import admin

from OrdersManager import Clients, Items, Orders

# Register your models here.

class ClientsAdmin( admin.ModelAdmin ):
    """ Modify the fields shown at table on panel admin """
    list_display = (  "name", "address", "phone" )
    search_fields= ("name", "phone")

class ItemsAdmin( admin.ModelAdmin ):
    list_filter=( "item_section", )
    
class OrdersAdmin( admin.ModelAdmin ):
    list_display=( "order_number", "order_date" )
    list_filter = ( "order_date" )
    date_hierarchy = "order_date"
 
# admin.site.register(Clients )
admin.site.register(Clients, ClientsAdmin )
admin.site.register(Items, ItemsAdmin)
admin.site.register(Orders, OrdersAdmin)


from django.db import models

# Create your models here.
class Clients( models.Model ):
    """ First table, Clients """
    name = models.CharField( max_length=30)
    address = models.CharField( max_length=50)
    email = models.EmailField( )
    phone = models.CharField( max_length=10 )

class Items( models.Model ):
    item_name = models.CharField( max_length=30 )
    item_section = models.CharField( max_length=20 )
    item_price = models.IntegerField()

class Orders(models.Model ):
    order_number = models.IntegerField()
    order_date = models.DateField( )
    order_delivered = models.BooleanField( )


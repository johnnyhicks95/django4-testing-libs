from django.db import models

# Create your models here.
class Clients( models.Model ):
    """ First table, Clients """
    name = models.CharField( max_length=30)
    address = models.CharField( max_length=50, verbose_name="La dirección"  )
    email = models.EmailField( blank=True, null=True )
    phone = models.CharField( max_length=10 )

class Items( models.Model ):
    item_name = models.CharField( max_length=30 )
    item_section = models.CharField( max_length=20 )
    item_price = models.IntegerField()
    
    def __str__(self):
        """ We return a label message like get() and print()"""
        return 'El nombre es %s la sección es %s y el precio es %s '%(self.item_name, self.item_section, self.item_price)

class Orders(models.Model ):
    order_number = models.IntegerField()
    order_date = models.DateField( )
    order_delivered = models.BooleanField( )


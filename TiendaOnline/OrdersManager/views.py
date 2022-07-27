from django.shortcuts import render

from django.http import HttpResponse
from OrdersManager import Items

# Create your views here.
def search_products( request ):
    """ Forms-search products """
    return render( request, "Orders_search.html" )

def search( request ):
    """ We bring the request from html input tag, name="prod" """
    if request.GET["prod"]:
        # msg_search= "Artículo buscado: %r" %request.GET["prod"]
        product_req = request.GET["prod"]
        # models.py - Items
        items_resp = Items.objects.filter( name_icontains = product_req ) 
        return render( 
                request, "Results_search_orders.html", 
                { #context
                "items_result": items_resp, 
                "query": product_req 
                } 
            ) 
        
    else:
        msg_search = "No has introducido algo para buscar"
    
    return HttpResponse( msg_search )

from django.shortcuts import render

from django.http import HttpResponse
from django.core.mail import send_mail
from OrdersManager import Items
from django.conf import settings

# Create your views here.
def search_products( request ):
    """ Forms-search products """
    return render( request, "Orders_search.html" )

def search( request ):
    """ We bring the request from html input tag, name="prod" """
    if request.GET["prod"]:
        # msg_search= "Artículo buscado: %r" %request.GET["prod"]
        product_req = request.GET["prod"]
        
        if len(product_req) > 20:
            msg_search = "Texto no válido, intenta con menos caracteres"
        
        else:
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



def contact(request):
    if request.method== "POST":
        subject = request.POST['subject_cont']
        message = request.POST['msg_cont'] + " "+ request.POST["email"]
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["direccionenviar@gmail.com"]
        
        send_mail( subject, message, email_from, recipient_list ) 
        
        return render( request, "Contact_msg_sent.html")
    
    return render(request,"Contact.html" )


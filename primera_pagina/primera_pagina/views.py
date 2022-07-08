#Views makes use of django,http
# Needs as first argument HttResponse, Htt

from django.http import HttpResponse
import datetime

def greetings(request):
    hi="""
    <html>
        <body>
        <h1>
        Hola hackers
        </h1>
        </body>
    </html>
    
    """
    return HttpResponse(hi)

def getCurrentDate( request ):
    #Getting current date
    now_date= datetime.datetime.now()
    
    html = """
    <html>
        <body>
        <h1>
        Fecha: %s
        </h1>
        </body>
    </html> 
    
    """ % now_date

    return HttpResponse(html)


def calculateAge( request, year ):
    #just calculates how many years from adding another parameter
    #trhough URL
    current_age = 18
    lapse = year - 2022
    future_age = current_age + lapse
    
    html = """
    <html>
        <body>
        <h2>
        En el año: %s, tendrás %s
        </h2>
        </body>
    </html> 
    
    """ % (year, future_age )
    
    return HttpResponse( html )
    
    
#Views makes use of django,http
# Needs as first argument HttResponse,

from django.http import HttpResponse
from django.template import Template, Context
import datetime
from django.shortcuts import render

class Persona(object):
     def __init__(self, name, last_name ):
         self.name = name
         self.last_name = last_name

def greetings(request):
    professor = Persona( "Sarah", "Fortuna" )
    
    name = "Juan"
    last_name = "Hicks"
    courses_list= ["Plantillas", "Modelos", "Formularios" ] 
    
    #Open external file in a variable
    # greeting_html = open(r"C:\Users\johnny\Desktop\Proyectos-Software\django-2022\django4-testing-libs\primera_pagina\primera_pagina\templates\greetings.html")
    #Create the variable template
    # temp = Template( greeting_html.read() )
    # Close the stream file
    # greeting_html.close()
    # Create the variable context, (may or not have dynamic content)
    # context can use dicts and objects
    # ctx = Context( {
    #     "person_name": name, "last_name": last_name,
    #     "prof_name": professor.name, "prof_last_name": professor.last_name,
    #     "themes_list": courses_list,
    # } )
    
    # Render the view
    # document = temp.render(ctx)
        
    # return HttpResponse(document) -> shortcuts render
    return render( request, 
        "greetings.html",
        {
         "person_name": name, "last_name": last_name,
         "prof_name": professor.name, "prof_last_name": professor.last_name,
         "themes_list": courses_list,
    } )

def courseC( request ):
    now_date= datetime.datetime.now()
    return render( request, "courses/CourseC.html", { "getNowDate": now_date } )
    
def courseCss( request ):
    # now_date= datetime.datetime.now()
    return render( request, "courses/CourseCss.html", { } )

def getCurrentDate( request ):
    #Getting current date
    now_date= datetime.datetime.now()
    now_day_date= datetime.datetime.now().day
    now_month_date= datetime.datetime.now().month
    
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
    
    
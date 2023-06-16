from django.shortcuts import render, HttpResponse


html_base = """
<h1>MI WEB PERSONAL</h1>
"<h1>MI WEB PERSONAL</h1><h2>Portada</h2>"
"""


def home(request):
    return render(request,"core/home.html")

def about(request):
    return render(request,"core/about.html")
def contact(request):
    return render(request,"core/contact.html")


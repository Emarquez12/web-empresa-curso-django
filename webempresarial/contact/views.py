import django
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
# Create your views here.


def contact(request):

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Enviamos Correos
            email = EmailMessage(
                "La Cafeteria Nuevo Mensaje de Contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.com",
                ["marquez.technologydev@gmail.com"],
                reply_to=[email]
                )
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
            except Exception as e:
                #Algo salio Mal
                return redirect(reverse('contact')+"?fail")
                
            

    contact_form = ContactForm()
    return render(request, "contact/contact.html",{"form":contact_form}) 

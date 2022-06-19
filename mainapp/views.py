from django.shortcuts import render

from django.core.mail import send_mail, send_mass_mail
from django.http import HttpResponse

from django.template import Context, Template

from django.template.loader import render_to_string
# Create your views here.
from .models import Victim

from .utils import send_bulk_email, send_bulk_html_string_email
def send_blast(request):
    tpl = " <h1>{{first_name}}</h1> "

    subject = "Bulk Mail"
    DEFAULT = "Raihan Ahmed <algorithm@tobuy.click>"

    LIST = Victim.objects.all()

    ok = send_bulk_html_string_email(LIST, subject, tpl, DEFAULT)
    return HttpResponse(ok)




# def send_blast(request):
#
#     tpl = Template(" <h1>{{name}}</h1> ")
#
#     subject = "Bulk Mail"
#     DEFAULT = "Raihan Ahmed <algorithm@tobuy.click>"
#
#     LIST = [
#         {'name':'Raihan', 'email':'raihan.tusher@yahoo.com'},
#         {'name':'Tusher', 'email':'raihan.tusher@yahoo.com'},
#     ]
#
#     mail_tuple = []
#     for l in LIST:
#         print(l)
#         message = tpl.render(Context(dict(name=l['name'])))
#         mail_tuple.append(
#             ( subject, message, DEFAULT, [ l['email'] ]  )
#         )
#
#     mail_tuple=send_mass_mail(mail_tuple)
#     return HttpResponse(mail_tuple)
#
#

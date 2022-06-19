from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.urls import reverse
from .models import CampaignList, Log
from mainapp.models import Victim
# Create your views here.
from django.core import mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.template import Template, Context
from django.contrib.sites.shortcuts import get_current_site

from mainapp.utils import send_bulk_html_string_email

from datetime import datetime

def run(request, id):
    current_site = get_current_site(request)

    campaign = CampaignList.objects.filter(id=id).first()

    if campaign.is_published == False:
        template = campaign.template

        subject = template.subject
        body = template.template_body
        body += "<img src='http://{{ domain }}{% url 'campaign:track' log %}' />"

        DEFAULT_FROM_EMAIL = template.from_mail

        email_list = Victim.objects.filter(list=campaign.list).all()
        print(email_list)

        emails = []
        for recipient in email_list:
            print(recipient.email)
            tpl = Template(body)

            log = Log.objects.create(campaign=campaign, email=recipient)
            html_content = tpl.render(Context(
                {
                    'email': recipient.email,
                    'first_name': recipient.first_name or " ",
                    'last_name': recipient.last_name or " ",
                    'domain': current_site,
                    'log': log.id

                }
            ))


            email = EmailMessage(subject, html_content, DEFAULT_FROM_EMAIL, [recipient.email])
            email.content_subtype = "html"

            # email = EmailMultiAlternatives(subject, text_content, from_email, [ recipient['email']])
            # email.attach_alternative(html_content,'html/text')
            emails.append(email)

        connection = mail.get_connection()
        connection.send_messages(emails)

        campaign.is_published  =True
        campaign.launched_at = datetime.now()
        campaign.save()
    context = {
        'opened': campaign.logs.filter(is_opened=True).count(),
        'not_opened': campaign.logs.filter(is_opened=False).count(),
        'campaign': campaign
    }
    return render(request, 'panel/campaign/report.html', context)

class PixelView(View):

    def get(self, request, *args, **kwargs):
        image_data = open(settings.BASE_DIR / 'static/tracker/0.gif', 'rb').read()
        log_id = kwargs.get('log_id')

        # email opened
        log = Log.objects.filter(id=log_id).first()
        log.is_opened = True
        log.save()

        ###Record somewhere that user_id has viewed the email

        return HttpResponse(image_data, content_type="image/png")

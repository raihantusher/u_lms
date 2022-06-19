from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core import mail


def send_bulk_email(emails_list, subject, context, template, from_email):
    html_content = render_to_string(template, context)
    text_content = strip_tags(html_content)
    emails = []
    for recipient in emails_list:
        email = EmailMultiAlternatives(subject, text_content, from_email, [recipient])
        email.attach_alternative(html_content, "text/html")
        emails.append(email)
    connection = mail.get_connection()
    return connection.send_messages(emails)


from django.template import Context, Template
from django.contrib.sites.shortcuts import get_current_site
from campaign.models import Log

def send_bulk_html_string_email(emails_list, subject, template, from_email, campaign):
    tpl = Template(template)
    emails = []
    for recipient in emails_list:

        html_content = tpl.render(Context(
            {
                'email': recipient.email,
                'first_name': recipient.first_name or " ",
                'last_name': recipient.last_name or " "

            }
        ))

        print(html_content)

        email = EmailMessage(subject, html_content, from_email, [recipient.email ])
        email.content_subtype = "html"

        # email = EmailMultiAlternatives(subject, text_content, from_email, [ recipient['email']])
        # email.attach_alternative(html_content,'html/text')
        emails.append(email)

    connection = mail.get_connection()
    return connection.send_messages(emails)

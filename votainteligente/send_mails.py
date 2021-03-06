# coding=utf-8
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.conf import settings

def send_mail(context_dict, template_prefix, to=[], reply_to=None, from_email=settings.DEFAULT_FROM_EMAIL):
    context = Context(context_dict)
    template_prefix_dict = {'template_prefix': template_prefix}
    template_body = get_template('mails/%(template_prefix)s_body.html' % template_prefix_dict)
    body = template_body.render(context)
    template_subject= get_template('mails/%(template_prefix)s_subject.html' % template_prefix_dict)
    subject = template_subject.render(context).replace('\n', '').replace('\r', '')
    email = EmailMessage(subject, body, from_email,
                        to)
    if reply_to is not None:
        email.reply_to = [reply_to]
    email.send()


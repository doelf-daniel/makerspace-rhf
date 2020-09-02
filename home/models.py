from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from django.utils import timezone
from wagtail.core.models import Page


class HomePage(Page):
    body = RichTextField(blank=True)
    date = models.DateTimeField(verbose_name="Post date", default=timezone.now)


    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),

    ]

    settings_panels = Page.settings_panels + [
        FieldPanel('date'),
    ]

from django import template
from django.apps import apps
import os

register = template.Library()

@register.filter
def verbose_name(obj):
	return obj.model._meta.verbose_name if getattr(obj, 'model', False) else obj.form_class._meta.model._meta.verbose_name

@register.filter
def verbose_name_plural(obj):
	return obj.model._meta.verbose_name_plural if getattr(obj, 'model', False) else obj.form_class._meta.model._meta.verbose_name_plural

@register.simple_tag
def get_model_verbose_name(app, model):
	return apps.get_model(app, model)._meta.verbose_name.title()

@register.simple_tag
def get_model_verbose_name_plural(app, model):
	return apps.get_model(app, model)._meta.verbose_name_plural.title()

@register.filter
def basename(value):
	return os.path.basename(value)

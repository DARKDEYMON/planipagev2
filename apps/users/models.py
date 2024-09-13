from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.

class User(AbstractUser):
	ci = models.CharField(
		verbose_name='C.I.',
		max_length=12,
		null=True,
		blank=True,
		unique=True,
		validators=[
			RegexValidator(
				regex=r'^([0-9]{7,8})(-[A-Z0-9]{2})?$',
				message='La cédula de identidad consta de 7 a 8 números, o 7 a 8 números y un complemento separado por guiones EJ 5567756 o 5567756-2B'
			),
		]
	)
	class Meta:
		verbose_name = _("user")
		verbose_name_plural = _("users")
		permissions = (
			("users", "Modulo de usuarios"),
			("tipos", "Modulo de Tipos "),
			("publicaciones", "Modulo de Publicaciones "),
			("extras", "Modulo Extras "),
		)

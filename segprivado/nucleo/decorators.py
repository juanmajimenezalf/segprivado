from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect

from nucleo.models import User


def paciente(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='home'):
   
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_paciente,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def medico(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='home'):
   
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_medico,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
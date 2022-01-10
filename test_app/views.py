from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.shortcuts import render
from test_app.forms import NumberForm
from django.urls import reverse
import random

from .psy import Psychics


def session_decorator(func):
    def wrapper(request):
        if 'psy_ids' not in request.session:
            psys = [Psychics() for __i in range(random.randint(2, 3))]
            request.session['psy_ids'] = psys
            request.session['user_history'] = []
            return HttpResponseRedirect(reverse('user_num'))
        else:
            return func(request)

    return wrapper


@session_decorator
def get_psy_list(request):
    user_history = request.session['user_history']
    psys = [psy for psy in request.session['psy_ids']]
    return render(request, 'test_app/index.html', {'phychics': psys, 'user_history': user_history})


@session_decorator
def potluck(request):
    psys = [psy for psy in request.session['psy_ids']]
    [psy.potluck() for psy in psys]
    return HttpResponseRedirect(reverse('write_num'))


@session_decorator
def get_your_choice(request):
    number_form = NumberForm()
    user_history = request.session['user_history']
    psys = [psy for psy in request.session['psy_ids']]
    return render(request, 'test_app/user_number.html',
                  {'phychics': psys, 'number_form': number_form, 'user_history': user_history})


@session_decorator
def check_result(request):
    number_form = NumberForm(request.POST)
    psys = [psy for psy in request.session['psy_ids']]
    if number_form.is_valid():
        [psy.check_answer(number_form.cleaned_data.get('number')) for psy in psys]
        request.session['user_history'].append(number_form.cleaned_data.get('number'))
        return HttpResponseRedirect(reverse('user_num'))
    else:
        return HttpResponseRedirect(reverse('write_num'))


class StartView(View):
    def get(self, request):
        result = get_psy_list(request)
        return result

    def post(self, request):
        result = potluck(request)
        return result


class InputNumberView(View):
    def get(self, request):
        result = get_your_choice(request)
        return result

    def post(self, request):
        result = check_result(request)
        return result

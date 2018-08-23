from django_micro import configure, route, run
from django.http import HttpResponse, HttpResponseRedirect
import requests
from memorised.decorators import memorise
import os

DEBUG = True
configure(locals())


def get_url(hash_code):
    url ="https://1fichier.com/?{}&auth=1".format(hash_code)
    auth_str = os.environ.get("USER_PASSWORD", "").split(":")
    resp = requests.get(url, auth=tuple(auth_str))
    try:
        resp.raise_for_status()
        return str(resp.content).split(";")[0]
    except:
        return "http://puya.si?msg=que querias hacer"


@route('', name='homepage')
def homepage(request):
    h = request.GET.get('hash')
    if h:
        url = get_url(h)
        return HttpResponseRedirect(url)

    return HttpResponse('mono')


application = run()


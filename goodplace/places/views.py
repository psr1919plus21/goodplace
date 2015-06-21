from django.forms.models import modelform_factory
from django.shortcuts import render_to_response 
from django.http import HttpResponse
from django.template import RequestContext, loader
import datetime
from .models import  Props, Photos

def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        
    })
    return HttpResponse(template.render(context))

def propose(request, prop_id):
    props = Props.objects.get(pk=prop_id)
    propPhotos = Photos.objects.filter(photoprop=props)
    template = loader.get_template('propose.html')
    context = RequestContext(request, {
        'props': props,
        'prop_id': prop_id,
        'propPhotos': propPhotos
    })
    return HttpResponse(template.render(context))

def proplist(request):
    props = Props.objects.order_by('-pub_date')
    template = loader.get_template('proplist.html')
    context = RequestContext(request, {
        'props': props
    })
    return HttpResponse(template.render(context))

def newad(request):
    propsFormSet = modelform_factory(Props, fields=('props_title', 'props_city', "pub_date"))
    template = loader.get_template('newad.html')
    if request.method == 'POST':
        formset = propsFormSet(request.POST)
        print formset.is_valid()
        today = datetime.date.today().isoformat()
        if formset.is_valid():
            formset.save()
    else:
        formset = propsFormSet()
    return render_to_response("newad.html", {
        "formset": formset,
        "today": today
    },
        RequestContext(request)
    )
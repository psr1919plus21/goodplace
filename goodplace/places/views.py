from django.http import HttpResponse
from django.template import RequestContext, loader
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
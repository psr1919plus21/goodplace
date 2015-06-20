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

def newad(request):
    propsFormSet = modelform_factory(Props, fields=('props_title', 'props_city', 'props_street', 'props_home', 'props_place', 'props_sleepplace', 'props_rating', 'props_state', 'props_price', 'props_postfix', 'props_authorname', 'props_authorlastname', 'props_authorpatronymic', 'props_authorphone', 'props_howater', 'props_internet', 'props_washmachine', 'props_furniture', 'props_linens', 'props_utensils', 'props_microwave', 'props_kids', 'props_pets', 'props_addinfo', 'pub_date'))
    template = loader.get_template('newad.html')
    if request.method == 'POST':
        formset = propsFormSet(request.POST, request.FILES)
        formset.save()

    return render_to_response("newad.html", {
        "formset": formset,
    })
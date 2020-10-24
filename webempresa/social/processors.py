from .models import Link

def ctx_dict(request): #Context Dictionary
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx
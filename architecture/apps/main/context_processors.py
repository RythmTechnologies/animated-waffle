from .models import Logo
from .mixin import HttpRequest, HttpResponse

def logo_context(request: HttpRequest) -> HttpResponse:
    logo = Logo.objects.first()  # Varsayılan olarak ilk logo'yu alır
    return {'site_logo': logo}

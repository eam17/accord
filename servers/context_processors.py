from .models import Server

def servers_var(request):
    servers = Server.objects.all()
    context = {
        "servers": servers,
    }
    return {"servers_var": servers}
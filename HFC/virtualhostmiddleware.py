virtual_hosts = {
    "hack-for-change.org": "HFCCore.urls",
    "staging.hack-for-change.org":"HFCCore.urls",
    "forchange.in": "TFC.urls",
    "staging.forchange.in":"TFC.urls",
    "*.staging.forchange.in":"TFC.urls",
    #local setup
    "www.staging.forchange.in:8000":"TFC.urls",
    "www.staging.hack-for-change.org:8000":"HFCCore.urls",
    #"forchange.in:8000": "TFC.urls"
    
}


class VirtualHostMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # let's configure the root urlconf
        host = request.get_host()
        print('hostname=', host)
        request.urlconf = virtual_hosts.get(host)
        print('urlgoes to=', request.urlconf)
    
        response = self.get_response(request)
        print(response)
        return response
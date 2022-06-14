from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.core.exceptions import PermissionDenied
import jwt
from django.conf import settings
from app.custom_exception import TokenNotFound,PermissionDenied

class AddValidationMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        try:
            if settings.AUTH == True:
                print(request.META["HTTP_AUTH_TOKEN"])
                if "HTTP_AUTH_TOKEN" in request.META:
                    token = request.META["HTTP_AUTH_TOKEN"].replace("Bearer ","")
                    try:
                        token.replace(" ","")
                        decode_token=jwt.decode(token,settings.SECRET_KEY,algorithms=["HS256"])
   
                    except Exception as Error:
                        return HttpResponseBadRequest('Invalid Token')
                    if "email" in decode_token:
                        if "@ojas.com" in decode_token['email']:
                            return self.get_response(request)
                        else:
                            return HttpResponse("Email not matched..!")
                            # raise PermissionDenied("Permisson Denied Token")
                return HttpResponseBadRequest(request)
            else:
                return self.get_response(request)
        except Exception:
            if request.path in ["/api/token/","/api/token/refresh/"]:
                return self.get_response(request)
            return HttpResponse("Please Insert a Token")
            # raise TokenNotFound("Please Insert a Token")
    def process_exception(self, request,exception):
        return HttpResponse(exception)
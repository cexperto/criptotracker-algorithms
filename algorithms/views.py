from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, Http404
from rest_framework.reverse import reverse


# Create your views here.
def home(request):
    return HttpResponse("Welcome to the CryptotrackerAPI!")


class Compound(APIView):
    def post(self, request):
        capital = float(request.data['capital'])
        interest = float(request.data['interes'])
        time = float(request.data['time'])
        monto=((1.0+interest/100)**time)*capital        
        compound_interes=monto-capital
        
        data={
            'compound_interes':compound_interes,
            'monto': monto            
            }
        return Response(data)

class Nominal(APIView):
    def post(self, request):
        n = float(request.data['nominal']) #nominal rate
        m = float(request.data['periods']) # number of periods
        if m>0 and n<=1:
            e = ((1+n/m)**m)-1
            if e<1:
                e = e*100
                data={
                    'nominal_rate': e
                }
                return Response(data)
            else:
                return Response('incorrect values')

        else:
            return Response('periods dont can be 0 or >1')

        
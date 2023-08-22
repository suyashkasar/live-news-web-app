from django.shortcuts import render
from rest-framework.response import Response
from rest_framework.decorators import api_view
from datetime import*

@api_view(["GET"])	
def dt(request):
	d=datetime.now().date()
	msg="server date=" + str(d)
	return Response({"msg":msg})

@api_view(["GET"])
def ti(request):
	d=datetime.now().time()
	msg="server tine=" + str(d)
	return Response({"msg":msg})

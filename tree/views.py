from django.shortcuts import render

def index(request):
	return render(request, 'tree/index.html', dict())

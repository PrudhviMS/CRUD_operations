from django.shortcuts import render, redirect, HttpResponse

from .models import Details

# Create your views here.

def index(request):
    display_details = Details.objects.values()
    Context = dict()
    Context['data'] = display_details
    return render(request, 'index.html', Context)

def Addetails(request):
    data = Details(name=request.POST.get('name'), url=request.POST.get('url'), number=request.POST.get('number'))
    data.save()
    return redirect("index")

def searchinput(request):
    search_query = request.GET.get('search', '')
    if search_query:
        search_results = Details.objects.filter(name__icontains=search_query)
        search_data = globals()
        search_data['data'] = search_results
        return render(request, 'index.html', search_data)

    else:
        print('Unavailable............')
        return render(request, 'index.html')

def find(request):
    s = Details.objects.get(pk=request.GET['q'])
    return render(request, 'find.html', {'record': s})

def update(request):
    record = Details.objects.get(pk=request.POST["txtid"])
    record.name = request.POST["txtname"]
    record.url = request.POST["txturl"]
    record.number = request.POST["txtnum"]
    record.save()
    return redirect("index")

def delete(request):
    s = Details.objects.get(pk=request.GET['q'])
    s.delete()
    return redirect("index")

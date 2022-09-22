from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

def show_mywatchlist(request):
    data_mywatchlist = MyWatchList.objects.all()
    context = {
        'list_barang' : data_mywatchlist,
        'nama': 'Mahmud Asrul',
        'npm': '2106655255'
    }
    return render(request, "mywatchlist.html", context)

def menerima_request_id_xml (request,id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def menerima_request_id_json(request,id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def menerima_fungsi_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def menerima_fungsi_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def menerima_fungsi_html(request):
    data_mywatchlist = MyWatchList.objects.all()
    context = {
        'list_barang' : data_mywatchlist,
        'nama': 'Mahmud Asrul',
        'npm': '2106655255'
    }
    return render(request, "mywatchlist.html", context)
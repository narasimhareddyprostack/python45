from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.


def getindexpage(request):
    eid = 101
    ename = 'Rahul'
    cdate = datetime.datetime.now()
    mydata = {'emp': {'eid': eid, 'ename': ename}, 'cdate': cdate}
    return render(request, 'index.html', context=mydata)


""" def getindexpage(request):
    eid = 101
    ename = 'Rahul'
    emp = {'eid': eid, 'ename': ename}
    # return HttpResponse("Welcome! Djanog")
    return render(request, 'index.html', context=emp)

 """

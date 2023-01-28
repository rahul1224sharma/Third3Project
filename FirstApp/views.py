from django.shortcuts import render
import datetime
# Create your views here.
def wishes3(request):
    date1=datetime.datetime.now()
    msg1='Hello User....GOOD';
    hr=int(date1.strftime('%H'))
    imgs='gm.jpg';
    if hr<12:
        msg1+='Morning !!';
        imgs='gm.jpg'
    elif hr<16:
        msg1+='AfterNoon';
        imgs='ga.jpg';
    elif hr<20:
        msg1+='Evening!!';
        imgs='ge.jpg';
    else :
        msg1+='Night'
        imgs='gn.jpg';
    dict1={'date1':date1,'msg1':msg1,'imgs':imgs}
    return render(request,'FirstApp/wishes3.html',context=dict1)

import datetime
def gallery(request):
    date1=datetime.datetime.now()
    msg='*****Django Image Gallery****'
    dict1={'date1':date1,'msg':msg}
    return render(request,'FirstApp/gallery.html',context=dict1)
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import NGO
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from core.views import message
import folium



# Finding nearby NGOss
def nearby(request):
    details=False
    lat=0.0
    long=0.0
    dist=""
    near=[]
    dirn=[]
    count=0

    if request.method == 'POST' and details==False:
        details=True
        lat=request.POST.get('lat')
        long=request.POST.get('long')
        location = fromstr(f'POINT({long} {lat})', srid=4326)
        dist=request.POST.get('dist')

        m=folium.Map(location=[lat,long],zoom_start=12)

        folium.Marker([lat,long], popup='', tooltip='Your Location!', icon=folium.Icon(color='red')).add_to(m),

        if dist=="lt1":
            near= NGO.objects.annotate(distance=Distance("location", location)/1000).filter(distance__lte=1).order_by("distance")
        elif dist=="lt5":
            near = NGO.objects.annotate(distance=Distance("location", location)/1000).filter(distance__lte=5).order_by("distance")
        elif dist=="lt10":
            near= NGO.objects.annotate(distance=Distance("location", location)/1000).filter(distance__lte=10).order_by("distance")
        elif dist=="lt15":
            near= NGO.objects.annotate(distance=Distance("location", location)/1000).filter(distance__lte=15).order_by("distance")
        else:
            near= NGO.objects.annotate(distance=Distance("location", location)/1000).filter(distance__lte=30).order_by("distance")
        #print(near)

        if len(near)>0:
            for it in near:
                org=it.name.replace(' ','+')
                org_address=it.address.replace(' ','+')
                link="https://www.google.com/maps/dir/?api=1&destination=" + org + "+"+org_address
                dirn.append(link)
                tooltip="Name:"+it.name
                folium.Marker([it.location.y,it.location.x], popup='<a href="' + link + '">GetDirection</a>', tooltip=tooltip).add_to(m)


        m.save('templates/donation/map_near_ngo.html')

    return render(request,'donation/nearby_NGO.html',{'near':near, 'details':details,'zi':zip(near,dirn)})



# Registration Form for NGOs
def ngo_form(request):
    name=""
    address=""
    city=""
    lat=0.0
    long=0.0
    details=False

    if request.method == 'POST' and details==False:
        details=True
        name = request.POST.get('name')
        address= request.POST.get('address')
        city= request.POST.get('city')
        lat=request.POST.get('lat')
        long=request.POST.get('long')
        location = fromstr(f'POINT({long} {lat})', srid=4326)

        s=NGO(name=name, city=city, address=address, location=location)
        s.save()
        return message(request,"Thank you for submitting your details")

    return render(request,'donation/ngo_form.html',{'details':details})


# Show user and nearly NGOs on map
def map_near_ngo(request):
    return render(request,'donation/map_near_ngo.html')
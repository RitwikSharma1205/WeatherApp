from django.shortcuts import render
import requests
def home(request):
    context={}
    if request.method=="POST":
        city=request.POST['city']
        url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=0894112720df32d2ebe6891971c6f0fa'
        data=requests.get(url).json()
        if(data['cod']=='404'):
            message=data['message']
            context={
                'error':message
            }
        else:
            payload={
                'city':data['name'],
                'weather':data['weather'][0]['main'],
                'icon':data['weather'][0]['icon'],
                'kelvintemperature':data['main']['temp'],
                'celciustemperature':int(data['main']['temp']-273),
                'pressure':data['main']['pressure'],
                'humidity':data['main']['humidity'],
                'description':data['weather'][0]['description'],
                'country':data['sys']['country']

            }
            context={'data':payload}
            return render(request,"weather/index.html",context)
    return render(request,"weather/index.html",context)

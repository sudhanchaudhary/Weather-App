from django.shortcuts import render
from django.contrib import messages
import requests
from decouple import config
from .current_time import time

# Create your views here.
def home(request):
    if 'city' in request.POST:
        city=request.POST.get('city')
    else:
        city='kathmandu'
    # weather_api=config('weather_api')
    # city_api=config('city_api')
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=d97e3d6a01acac1e658894664f74a548'
    param={'units':'metric'}
    data=requests.get(url,param).json()
    image_url=f'https://api.unsplash.com/search/photos?query={city}&per_page=1&client_id=ogpUuxNpc99f56CDbbzOzrmunQqkpVvFL4mlO_P-Spg'
    response=requests.get(image_url).json()
    
    try:
        image=response['results'][0]['urls']['regular']
        temp=data['main']['temp']
        weather=data['weather'][0]['description']
        wind=data['wind']['speed']
        humidity=data['main']['humidity']
        pressure=data['main']['pressure']
        visibility=data['visibility']/1000
        feels_like=data['main']['feels_like']
        min_temp=data['main']['temp_min']
        max_temp=data['main']['temp_max']
        weather_cond=data['weather'][0]['main']
    except:
        image = None
        wind = 0
        humidity = 0
        pressure = 0
        visibility = 0
        feels_like = 0
        min_temp = 0
        max_temp = 0
        weather_cond = 0
        temp= 0
        weather= city
        messages.error(request,'City not found')
        
    context={
        'image':image,
        'temp':temp,
        'city':city,
        'weather':weather,
        'wind':wind,
        'humidity':humidity,
        'pressure':pressure,
        'visibility':visibility,
        'feels':feels_like,
        'min':min_temp,
        'max':max_temp,
        'condition':weather_cond,
        }
    return render(request,'index.html',context)
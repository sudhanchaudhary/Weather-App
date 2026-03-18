# Fully functional weather app
 This is a fully functional weather app whick shows the temperature, weather condition, humidity, wind speed , visibility, pressure and image of any city in the world. It is build by fetching data from Openweather API and city image from Unsplash API

---

## Features
1. Temp
2. Weather condition
3. Wind speed
4. humidity
5. Pressure
6. Visibility
7. City image

---
| S.N | Front-end | Backend | API |
|-----|-----------|---------|-----------|
| 1 | Html | Python | openweather |
| 2 | Css |  Django  | unsplash |
| 3 | Bootstrap | 
| 4 | JS | 

---
## Steps to use the app
1. Install the requiremants.txt and activate venv
   ```
   pip install -r requiremants.txt
   ./myenv/Scripts/activate
   ```
   
2. clone git repo in the folder
   
   ```
    git clone https://github.com/sudhanchaudhary/Weather-App.git
   ```
   
3.Create your oun openweather and unsplash api key and paste the keys in line no. 13 and 14 of views.py file respectively.
4.create your owm secret key and paste in settings.py
5.run the local server

   ```
   python manage.py runserver
   ```
---
***Note*** *Follow the link to create your own api key*

*1. [Openewather](http://openweathermap.org/api)*

*2. [Unsplash](https://unsplash.com/developers)*

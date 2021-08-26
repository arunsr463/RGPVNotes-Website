from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('login', views.login, name="login"),
    path('registration', views.registration, name="registration"),
    path('computerScienceIndexPage', views.computerScienceIndexPage, name="computerScienceIndexPage"),
    path('service', views.service, name="service"),
    path('contact', views.contact, name="contact"),
    path('computerScience', views.computerScience, name="computerScience"),
    path('mechanical', views.mechanical, name="mechanical"),
    path('civil', views.civil, name="civil"),
    path('informationAndTechnology', views.informationAndTechnology, name="informationAndTechnology"),
    path('engineeringDrawing', views.engineeringDrawing, name="engineeringDrawing"),
    path('engineeringChemistry', views.engineeringChemistry, name="engineeringChemistry"),
    path('mathematics1',views.mathematics1, name="mathematics1"),
    path('english',views.english, name="english"),
    path('engineeringPhysics',views.engineeringPhysics, name="engineeringPhysics"),
    path('mathematics2',views.mathematics2, name="mathematics2"),
    path('basicComputerEngineering',views.basicComputerEngineering, name="basicComputerEngineering"),
    path('basicCivilAndMechanicsEngineering',views.basicCivilAndMechanicsEngineering, name="basicCivilAndMechanicsEngineering"),
    path('basicMechanicalEngineering',views.basicMechanicalEngineering, name="basicMechanicalEngineering"),
    path('basicElectricalAndElectronics',views.basicElectricalAndElectronics, name="basicElectricalAndElectronics")
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name="home"),
    path('clubs/aero_modelling', views.amc , name="amc"),
    path('clubs/astronomy', views.astro , name="astro"),
    path('clubs/cops', views.cops , name="cops"),
    path('clubs/csi', views.csi , name="csi"),
    path('clubs/robotics', views.robotics , name="robotics"),
    path('clubs/sae', views.sae , name="sae"),
    path('clubs/biz', views.biz , name="biz"),
    path('certificates', views.certificates , name="certificates"),
    path('tac', views.inventory , name="tac"),
    path('others/bigbook', views.inventory , name="bigbook"),
    path('team', views.team , name="team"),
    path('learning', views.learning , name="learning"),
    path('verification', views.verification , name="verification"),
    path('blog', views.blog , name="blog"),
    path('udaan', views.udaan , name="udaan"),
    path('app', views.app , name="app"),
]
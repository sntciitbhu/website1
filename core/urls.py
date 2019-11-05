from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
#from django.contrib.auth.views import logout

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
    ##authentication urls
    #path('accounts/', include('django.contrib.auth.urls')),
    path('signin/', views.signin, name="signin"),
    path('postsign/', views.postsign, name="postsign"),
    path('reset_password/', views.resetpassword, name="resetpassword"),
    path('postresetpassword/', views.postresetpassword, name='postresetpassword'),
    path('signup/', views.signup, name="signup"),
    path('postsignup/', views.postsignup, name="postsignup"),
    ##
    path('index/<email>/<user>/', views.index, name="index"),
    path('logout/', auth_views.LogoutView.as_view() , {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    #path('logout/', views.logout, name="logout"),
    path('addactivity/', views.addactivity, name="addactivity"),
]
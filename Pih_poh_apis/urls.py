"""
URL configuration for Pih_poh_apis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pihpoh.views import HomeView,SignupListView,SignupCreateView,LoginAPIView,DanceLevelListView, DanceLevelCreateView, DanceLevelUpdateView, DanceLevelDeleteView,InterestLevelListView, InterestLevelCreateView, InterestLevelUpdateView,InterestLevelDeleteView,StyleLevelListView, StyleLevelCreateView, StyleLevelUpdateView, StyleLevelDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",HomeView.as_view(),name="home"),

    path('get/signup/', SignupListView.as_view(), name='signup-list'),

    path('post/signup/', SignupCreateView.as_view(), name='signup-create'),

    path('post/login/', LoginAPIView.as_view(), name='login'),

    path('GetDancelevel/', DanceLevelListView.as_view(), name='DanceLevel-list'),
    
    path('PostDancelevel/', DanceLevelCreateView.as_view(), name='DanceLevel-create'),

    path('PutDancelevel/<int:id>/', DanceLevelUpdateView.as_view(), name='DanceLevel-update'),  # PUT for update

    path('DeleteDancelevel/<int:id>/', DanceLevelDeleteView.as_view(), name='DanceLevel-delete'),  # DELETE for delete

    # Interest Level URLs
    path('GetInterest/', InterestLevelListView.as_view(), name='InterestLevel-list'),

    path('PostInterest/', InterestLevelCreateView.as_view(), name='InterestLevel-create'),

    path('PutInterest/<int:id>/', InterestLevelUpdateView.as_view(), name='InterestLevel-update'),  # PUT for update

    path('DeleteInterest/<int:id>/', InterestLevelDeleteView.as_view(), name='InterestLevel-delete'),  # DELETE for delete

    # Style Level URLs
    path('GetStyle/', StyleLevelListView.as_view(), name='StyleLevel-list'),

    path('PostStyle/', StyleLevelCreateView.as_view(), name='StyleLevel-create'),

    path('PutStyle/<int:id>/', StyleLevelUpdateView.as_view(), name='StyleLevel-update'),  # PUT for update

    path('DeleteStyle/<int:id>/', StyleLevelDeleteView.as_view(), name='StyleLevel-delete'),  # DELETE for delete

]

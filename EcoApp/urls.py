from django.urls import path

from EcoApp import views, adminviews, customerviews, authorityviews, dealerviews

urlpatterns=[
    path('',views.indexpage,name="indexpage"),
    path('loginpage',views.loginpage,name="loginpage"),
    path('reg_drop',views.reg_drop,name="reg_drop"),
    path('user_reg',views.user_reg,name='user_reg'),
    path('base',views.base,name='base'),
    path('dealer_reg',views.dealer_reg,name='dealer_reg'),
    path('authority',views.authority,name='authority'),
    path('adminpage',views.adminpage,name='adminpage'),
    path('customepage',views.customepage,name='customepage'),
    path('dealerpage',views.dealerpage,name='dealerpage'),
    path('dealerwelcomepage',views.dealerwelcomepage,name='dealerwelcomepage'),
    path('authoritypage',views.authoritypage,name='authoritypage'),
    path('log_out',views.log_out,name='log_out'),


    path('view_cus',adminviews.view_cus,name='view_cus'),
    path('view_dealer',adminviews.view_dealer,name='view_dealer'),
    path('tap_authority',adminviews.tap_authority,name='tap_authority'),
    path('add_authority',adminviews.add_authority,name='add_authority'),
    path('view_authority',adminviews.view_authority,name='view_authority'),
    path('approve_customer/<int:id>/',adminviews.approve_customer,name='approve_customer'),
    path('reject_customer/<int:id>/',adminviews.reject_customer,name='reject_customer'),
    path('approve_dealer/<int:id>/',adminviews.approve_dealer,name='approve_dealer'),
    path('reject_dealer/<int:id>/',adminviews.reject_dealer,name='reject_dealer'),
    path('ad_view',adminviews.ad_view,name='ad_view'),
    path('reject_ad/<int:id>/',adminviews.reject_ad,name='reject_ad'),



    path('scrapadd',customerviews.scrapadd,name='scrapadd'),
    path('scrap_view',customerviews.scrap_view,name='scrap_view'),


    path('view_ads_au',authorityviews.view_ads_au,name='view_ads_au'),
    path('approve_ad/<int:id>/',authorityviews.approve_ad,name='approve_ad'),

    path('ads',dealerviews.ads,name="ads"),

]
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('register',views.RegisterPage,name="registerpage"),
    path('login',views.LoginPage,name="loginpage"),
    path('signout',views.SignoutPage,name="signoutpage"),
    path('',views.IndexPage,name="indexpage"),
    path('add',views.AddPage,name="addpage"),
    path('edit',views.EditPage,name="editpage"),
    path('delete',views.DeletePage,name="deletepage"),
    path('user',views.UserPage,name="userpage"),
    path('addcart',views.AddCartPage,name="addcartpage"),
    path('cart',views.CartPage,name="cartpage"),
    path('details',views.DetailsPage,name="detailspage"),
    path('review',views.ReviewPage,name="reviewpage"),
    path('sub_review',views.Sub_ReviewPage,name="sub_reviewpage"),

]

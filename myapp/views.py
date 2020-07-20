from django.shortcuts import render,HttpResponse,HttpResponseRedirect,reverse
from . models import *
from . import urls

# Create your views here.

def RegisterPage(request):
    if request.method == "POST":
        u_type = request.POST.get("User type")
        uname = request.POST.get("u_name")
        gndr = request.POST.get("gender")
        m_no = request.POST.get("mob_no")
        eid = request.POST.get("emailid")
        pwd = request.POST.get("password")
        cpwd = request.POST.get("re_password")
        print("=====\n",u_type,uname,gndr,eid,pwd,cpwd,"\n=====")

        u_list = Admin.objects.filter(Username=uname)
        if u_list:
            message = "User Name already exist!"
            return render(request,"myapp/register.html",{'msg':message})

        e_list = Admin.objects.filter(Emailid=eid)
        if e_list:
            message = "Email id already exist!"
            return render(request,"myapp/register.html",{'msg':message})

        if pwd!=cpwd:
            message = "Password does not match!"
            return render(request,'myapp/register.html',{'msg':message})

        crt = Admin.objects.create(User_type=u_type, Username=uname, Gender=gndr, Mobile_no=m_no, Emailid=eid, Password=pwd)


        return HttpResponseRedirect(reverse('loginpage'))
    return render(request,"myapp/register.html")

def LoginPage(request):
    if request.method == "POST":
        u_type = request.POST.get("User type")
        eid = request.POST.get("emailid")
        pwd = request.POST.get("password")
        checked = Admin.objects.filter(User_type=u_type,Emailid=eid,Password=pwd)
        if checked:
            request.session['user_type'] = checked[0].User_type
            request.session['username'] = checked[0].Username
            request.session['email'] = checked[0].Emailid
            if u_type=="Admin":
                return HttpResponseRedirect(reverse('indexpage'))
            else:
                return HttpResponseRedirect(reverse('userpage'))
        else:
            message = "User type or Email id or Password is incorrect!"
            return render(request,"myapp/login.html",{'msg':message})
    return render(request,"myapp/login.html")

def SignoutPage(request):
    if  request.session.get('email') and request.session.get('user_type'):

        P_Name = request.POST.get("page_name")
        if request.method == "POST":
            if request.session['username']:
                del request.session['user_type']
                del request.session['username']
                del request.session['email']
            return HttpResponseRedirect(reverse('loginpage'))
        return render(request,"myapp/"+P_Name+".html")

    else:
        return HttpResponseRedirect(reverse('loginpage'))

def IndexPage(request):
    if  request.session.get('email') and request.session.get('user_type')=="Admin":
        detail_obj = Details.objects.all()
        return render(request,"myapp/index.html",{'detail':detail_obj})
    else:
        return HttpResponseRedirect(reverse('loginpage'))

def AddPage(request):
    if  request.session.get('email') and request.session.get('user_type')=="Admin":

        if request.method == "POST":

            mstr_obj = Master.objects.all()

            if request.POST.get("p_name"):
                
                # prod_id = request.POST.get("p_id")
                prod_name = request.POST.get("p_name")
                prod_price = request.POST.get("p_price")
                prod_image = request.FILES.get("p_img")
                prod_model = request.POST.get("p_model")
                prod_ram = request.POST.get("p_ram")
                prod_detail = request.POST.get("p_detail")

                # prod_id = int(prod_id)
                prod_price = int(prod_price)
                prod_ram = int(prod_ram)

                # p_list = Master.objects.filter(Product_id=prod_id)
                u_list = Master.objects.filter(Product_name=prod_name)
                # b_list = Master.objects.filter(Product_id=prod_id,Product_name=prod_name)

                if u_list:
                    pass
                else:
                    crt1 = Master.objects.create(Product_name=prod_name)

                crt1_obj = Master.objects.filter(Product_name=prod_name)
                print("============================================== : ",crt1_obj)
                
                if prod_image:
                    crt2 = Details.objects.create(Product_name_details=crt1_obj[0], Product_price=prod_price, Product_image=prod_image, Product_model=prod_model, Product_ram=prod_ram, Product_detail=prod_detail)
                else:
                    crt2 = Details.objects.create(Product_name_details=crt1_obj[0], Product_price=prod_price, Product_model=prod_model, Product_ram=prod_ram, Product_detail=prod_detail)

                return HttpResponseRedirect(reverse('indexpage'))
            else:
                return render(request,"myapp/add.html",{'mstr':mstr_obj})

        return render(request,"myapp/add.html")

    else:
        return HttpResponseRedirect(reverse('loginpage'))
    

def EditPage(request):
    if request.session.get('email') and request.session.get('user_type')=="Admin":

        if request.method == "POST":
            ed_id = request.POST.get("id_edit")
            print("edit id ==================== :",ed_id)
            detail_obj = Details.objects.get(pk=int(ed_id))
            print("edit obj ==================== :",detail_obj)
            if request.POST.get("p_name"):
                detail_obj.Product_name_details.Product_name = request.POST.get("p_name")
                detail_obj.Product_price = request.POST.get("p_price")
                if request.FILES.get("p_img"):
                    detail_obj.Product_image = request.FILES.get("p_img")
                detail_obj.Product_model = request.POST.get("p_model")
                detail_obj.Product_ram = request.POST.get("p_ram")
                detail_obj.Product_detail = request.POST.get("p_detail")
                detail_obj.Product_name_details.save()
                detail_obj.save()
                return HttpResponseRedirect(reverse('indexpage'))
            else:
                return render(request,"myapp/edit.html",{'detail':detail_obj})
        
        return render(request,"myapp/edit.html")
    else:
        return HttpResponseRedirect(reverse('loginpage'))

def DeletePage(request):
    if request.session.get('email') and request.session.get('user_type')=="Admin":

        if request.method == "POST":

            user_id = request.POST.get("id_del")
            user_obj = Details.objects.filter(pk=user_id)
            user_obj.delete()
            return HttpResponseRedirect(reverse('indexpage'))

        return render(request,"myapp/index.html")

    else:
        return HttpResponseRedirect(reverse('loginpage'))

def UserPage(request):
    if request.session.get('email') and request.session.get('user_type')=='Product Manager':
        detail_obj = Details.objects.all()
        return render(request,"myapp/Card_html_1.html",{'detail':detail_obj})
    else:
        return HttpResponseRedirect(reverse('loginpage'))

def AddCartPage(request):
    if request.session.get('email') and request.session.get('user_type')=='Product Manager':
        return HttpResponse("Added to Cart Page")
    else:
        return HttpResponseRedirect(reverse('loginpage'))

def CartPage(request):
    if request.session.get('email') and request.session.get('user_type')=='Product Manager':
        return HttpResponse("Welcome to Cart Page")
    else:
        return HttpResponseRedirect(reverse('loginpage'))

def DetailsPage(request):
    if request.session.get('email') and request.session.get('user_type')=='Product Manager':
        det_id = request.POST.get("detai_id")
        print("=============",det_id)
        det_obj = Details.objects.filter(pk=det_id)
        print("Details Objects =================================== : ",det_obj)
        print("Details Objects =================================== : ",det_obj[0])
        print("Details Objects Image =================================== : ",det_obj[0].Product_image)
        user_check = Admin.objects.filter(Username=request.session.get('username'),Emailid=request.session.get('email'))
        obj = Reviews.objects.filter(Prod_details=det_obj[0], User_details=user_check[0])
        
        all_obj = Reviews.objects.filter(Prod_details=det_obj[0]).order_by('-R_created_at')

        # u_rp_id = request.POST.get("rply_id")
        # rev_obj = Reviews.objects.filter(pk=u_rp_id)

        det_obj_z = Reviews.objects.filter(Prod_details=det_obj[0])
        print("=================================== : ",det_obj_z)


        
        if det_obj_z:
            all_rply_obj = Sub_Reviews.objects.filter(Reviews_replies=det_obj_z[0])
            
            # all_rply_obj = Sub_Reviews.objects.filter(Reviews_replies=rev_obj[0])
            
            if obj:
                return render(request,"myapp/Card_html_2.html",{'all':all_obj,'all_rply':all_rply_obj,'detail_obj':det_obj[0],'rev_obj':obj[0]})
            else:
                return render(request,"myapp/Card_html_2.html",{'all':all_obj,'all_rply':all_rply_obj,'detail_obj':det_obj[0]})
        
        else:
            if obj:
                return render(request,"myapp/Card_html_2.html",{'all':all_obj,'detail_obj':det_obj[0],'rev_obj':obj[0]})
            else:
                return render(request,"myapp/Card_html_2.html",{'all':all_obj,'detail_obj':det_obj[0]})
    
    
    else:
        return HttpResponseRedirect(reverse('loginpage'))

def ReviewPage(request):
    if request.session.get('email') and request.session.get('user_type')=='Product Manager':
        det_id = request.POST.get("detai_id")
        u_rev = request.POST.get("u_review")
        det_obj = Details.objects.filter(pk=int(det_id))

        user_check = Admin.objects.filter(Username=request.session.get('username'),Emailid=request.session.get('email'))
        try_obj = Reviews.objects.filter(Prod_details=det_obj[0], User_details=user_check[0])
        all_obj = Reviews.objects.filter(Prod_details=det_obj[0]).order_by('-R_created_at')

        if try_obj:
            return render(request,"myapp/Card_html_2.html",{'all':all_obj,'detail_obj':det_obj[0]})
        else:
            crt_obj = Reviews.objects.create(Prod_details=det_obj[0], User_details=user_check[0], User_reviews=u_rev)
            obj = Reviews.objects.filter(Prod_details=det_obj[0], User_details=user_check[0], User_reviews=u_rev)
            return render(request,"myapp/Card_html_2.html",{'all':all_obj,'rev_obj':obj[0],'detail_obj':det_obj[0]})
    else:
        return HttpResponseRedirect(reverse('loginpage'))

def Sub_ReviewPage(request):
    if request.session.get('email') and request.session.get('user_type')=='Product Manager':

        det_id = request.POST.get("detai_id")
        det_obj = Details.objects.filter(pk=int(det_id))

        u_rev_id = request.POST.get("rev_id")
        # u_rp_name = request.POST.get("rply_un")
        # u_rp_mail = request.POST.get("rply_em")
        u_rply = request.POST.get("u_rply")

        rev_id_obj = Reviews.objects.filter(pk=u_rev_id)

        user_check = Admin.objects.filter(Username=request.session.get('username'),Emailid=request.session.get('email'))
        
        rev_obj = Reviews.objects.filter(Prod_details=det_obj[0], User_details=user_check[0])

        all_obj = Reviews.objects.filter(Prod_details=det_obj[0]).order_by('-R_created_at')

        # all_rply_obj = Sub_Reviews.objects.filter(Reviews_replies=rev_id_obj[0])

        all_rply_obj = Sub_Reviews.objects.filter(Reviews_replies=rev_id_obj[0], Rply_user_details=user_check[0])
        
        if rev_obj:

            if all_rply_obj:
                return render(request,"myapp/Card_html_2.html",{'all':all_obj,'all_rply':all_rply_obj,'detail_obj':det_obj[0],'rev_obj':rev_obj[0]})
            else:
                crt_obj = Sub_Reviews.objects.create(Reviews_replies=rev_id_obj[0], Rply_user_details=user_check[0], User_replies=u_rply)
                obj = Sub_Reviews.objects.filter(Reviews_replies=rev_id_obj[0])
                return render(request,"myapp/Card_html_2.html",{'all':all_obj,'all_rply':obj,'detail_obj':det_obj[0],'rev_obj':rev_obj[0]})
        
        else:

            if all_rply_obj:
                return render(request,"myapp/Card_html_2.html",{'all':all_obj,'all_rply':all_rply_obj,'detail_obj':det_obj[0]})
            else:
                crt_obj = Sub_Reviews.objects.create(Reviews_replies=rev_id_obj[0], Rply_user_details=user_check[0], User_replies=u_rply)
                obj = Sub_Reviews.objects.filter(Reviews_replies=rev_id_obj[0])
                return render(request,"myapp/Card_html_2.html",{'all':all_obj,'all_rply':obj,'detail_obj':det_obj[0]})

    else:
        return HttpResponseRedirect(reverse('loginpage'))


# def Sub_ReviewPage(request):
#     if request.session.get('email') and request.session.get('user_type')=='Product Manager':

#         det_id = request.POST.get("detai_id")
#         det_obj = Details.objects.filter(pk=int(det_id))

#         u_rp_id = request.POST.get("rply_id")
#         u_rp_name = request.POST.get("rply_un")
#         u_rp_mail = request.POST.get("rply_em")
#         u_rply = request.POST.get("u_rply")
#         rev_admin = Admin.objects.filter(Username=u_rp_name,Emailid=u_rp_mail)
#         # print("-------------------------------------------------",u_rp_id,u_rp_mail,u_rp_name,rev_admin)
        
#         user_check = Admin.objects.filter(Username=request.session.get('username'),Emailid=request.session.get('email'))
        
#         det_obj_d = Reviews.objects.filter(User_details=rev_admin[0], Prod_details=det_obj[0])
#         print("-------------------------------------------------",det_obj_d)
#         all_rply_obj = Sub_Reviews.objects.filter(Reviews_replies=det_obj_d[0])

#         sv_rp_det = Reviews.objects.filter(User_details=user_check[0], Prod_details=det_obj[0])

#         rev_object = Reviews.objects.filter(Prod_details=det_obj[0], User_details=user_check[0])
#         all_obj = Reviews.objects.filter(Prod_details=det_obj[0]).order_by('-R_created_at')

#         if all_rply_obj:
#             if rev_object:
#                 return render(request,"myapp/Card_html_2.html",{'all':all_obj,'all_rply':all_rply_obj,'detail_obj':det_obj[0],'rev_obj':rev_object[0]})
#             else:
#                 return render(request,"myapp/Card_html_2.html",{'all':all_obj,'all_rply':all_rply_obj,'detail_obj':det_obj[0]})
        
#         else:
#             if rev_object:
#                 crt_obj = Sub_Reviews.objects.create(Reviews_replies=sv_rp_det[0], User_replies=u_rply)
#                 obj = Sub_Reviews.objects.filter(Reviews_replies=sv_rp_det[0])
#                 return render(request,"myapp/Card_html_2.html",{'all':all_obj,'all_rply':obj,'detail_obj':det_obj[0],'rev_obj':rev_object[0]})
#             else:
#                 crt_obj = Sub_Reviews.objects.create(Reviews_replies=sv_rp_det[0], User_replies=u_rply)
#                 obj = Sub_Reviews.objects.filter(Reviews_replies=sv_rp_det[0])
#                 return render(request,"myapp/Card_html_2.html",{'all':all_obj,'all_rply':obj,'detail_obj':det_obj[0]})
            
#     else:
#         return HttpResponseRedirect(reverse('loginpage'))


# def Sub_ReviewPage(request):
#     if request.session.get('email') and request.session.get('user_type')=='Product Manager':

#         u_r_id = request.POST.get("detai_id")
#         det_obj_d = Details.objects.filter(pk=int(u_r_id))

#         u_rp_id = request.POST.get("rply_id")
#         u_rp_name = request.POST.get("rply_un")
#         u_rp_mail = request.POST.get("rply_em")
#         u_rply = request.POST.get("u_rply")
#         rev_admin = Admin.objects.filter(Username=u_rp_name,Emailid=u_rp_mail)
#         det_obj = Reviews.objects.filter(pk=int(u_rp_id), User_details=rev_admin[0], Prod_details=det_obj_d[0])
#         all_rply_obj = Sub_Reviews.objects.filter(Reviews_replies=det_obj[0])
        
#         user_check = Admin.objects.filter(Username=request.session.get('username'),Emailid=request.session.get('email'))
#         rev_object = Reviews.objects.filter(Prod_details=det_obj_d[0], User_details=user_check[0])
#         all_obj = Reviews.objects.filter(Prod_details=det_obj_d[0]).order_by('-R_created_at')

#         if all_rply_obj:
#             if rev_object:
#                 return render(request,"myapp/Card_html_2.html",{'all':all_obj,'all_rply':all_rply_obj,'detail_obj':det_obj_d[0],'rev_obj':rev_object[0]})
#             else:
#                 return render(request,"myapp/Card_html_2.html",{'all':all_obj,'all_rply':all_rply_obj,'detail_obj':det_obj_d[0]})
        
#         else:
#             if rev_object:
#                 crt_obj = Sub_Reviews.objects.create(Reviews_replies=det_obj[0], User_replies=u_rply)
#                 obj = Sub_Reviews.objects.filter(Reviews_replies=det_obj[0], User_replies=u_rply)
#                 return render(request,"myapp/Card_html_2.html",{'all':all_obj,'all_rply':all_rply_obj,'reply_obj':obj[0],'detail_obj':det_obj_d[0],'rev_obj':rev_object[0]})
#             else:
#                 crt_obj = Sub_Reviews.objects.create(Reviews_replies=det_obj[0], User_replies=u_rply)
#                 obj = Sub_Reviews.objects.filter(Reviews_replies=det_obj[0], User_replies=u_rply)
#                 return render(request,"myapp/Card_html_2.html",{'all':all_obj,'all_rply':all_rply_obj,'reply_obj':obj[0],'detail_obj':det_obj_d[0]})
            
#     else:
#         return HttpResponseRedirect(reverse('loginpage'))

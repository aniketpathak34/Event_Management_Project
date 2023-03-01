from django.shortcuts import render, HttpResponseRedirect,HttpResponse
from .models import gallery, Services, videoContent, contactUs
from django.contrib import messages
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings



@login_required
def saveDataAdmin(request):
    final = 0
    if request.method == "POST":
            temp = gallery()
            temp.eventName = request.POST.get('eventName')
            temp.eventPlace = request.POST.get('eventPlace')
            temp.eventDescription = request.POST.get('eventDescription')
            temp.eventDate = request.POST.get("eventDate")
            
            if len(request.FILES) != 0:
                 temp.eventImageOne = request.FILES['imgOne']
                 temp.eventImageTwo = request.FILES['imgTwo']
                 temp.eventImageThree = request.FILES['imgThree']

            temp.save()
            messages.success(request, "your data is added to database")

        
            return render(request, 'eventAdminApp/adminPage.html')

    return render(request, 'eventAdminApp/adminPage.html')
    



def galleryTemplate(request):
    
    galler=gallery.objects.all()[::-1]

    data = {
        'serviceData' : galler 
    }
    return render(request, 'hpevent/gallery.html', data)



@login_required
def editAdmin(request):
    
    galler=gallery.objects.all()[::-1]
    videoInputData = videoContent.objects.all()[::-1]

    data = {
        'eventData' : galler, 
        'VIdata':videoInputData
    }
    return render(request, 'eventAdminApp/editAdmin.html', data)



@login_required
def deleteData(request, id):
     if request.method == "POST":
          pi = gallery.objects.get(pk=id)
          pi.delete()
          return HttpResponseRedirect('/DetailsAdmin/')


@login_required
def deleteVideo(request, id):
    if request.method == "POST":
        pu = videoContent.objects.get(pk=id)
        pu.delete()
        return HttpResponseRedirect('/DetailsAdmin/')


@login_required
def updateData(request, id):
  mymember = gallery.objects.get(id=id)
  template = loader.get_template('eventAdminApp/updateUser.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))



def hpServices(request):
    eventData = Services.objects.all()
    videoData = videoContent.objects.all()[:3:-1]
    clientData = gallery.objects.all()[:3:-1]
    # print(fi)
    data = {
         'eventData':eventData,
         'videodata':videoData,
         'clientdata':clientData,
    }
    return render(request, 'hpevent/hpindex.html', data)




def videoGallery(request):
    obj = videoContent.objects.all()[::-1]
    data = {
        'obj':obj
    }
    return render(request,'hpevent/videoGallery.html', data)




@login_required
def vInput(request):
    if request.method == "POST":
        temp = videoContent()
        temp.eventName = request.POST.get('vtitle')
        temp.eventCaption = request.POST.get('vdesc')
        temp.video = request.POST.get('vlink')   
        temp.save()
        messages.success(request, "your data is added to database")

        
        return render(request, 'eventAdminApp/vinput.html')

    return render(request, 'eventAdminApp/vinput.html')


# def login(request):
#     return render(request, 'eventAdminApp/login.html')


def my_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/DetailsAdmin/')
        else:
            return HttpResponseRedirect("<h1> enterd wrong credentials</h1>")
            ...
    else:
        return render(request, 'eventAdminApp/login.html')


def hpEventContact(request):
    messages.warning(request, '')
    
    if request.method == "POST":
        n1 = request.POST.get('name')
        n2 = request.POST.get('email')
        n3 = request.POST.get('numberone')
        n4 = request.POST.get('message')
        
        contact=contactUs(name=n1, email=n2, number=n3, message=n4)
        contact.save()
        
        messages.success(request, 'Thank you! your form succesfuly submited, We Will Contact You With in 24 Hours')
    return render(request, 'hpevent/contact.html')
























# def updaterecord(request, id):

#   if request.method == "POST":
#         temp = gallery.objects.get(id=id)
#         n1 = request.post.get('eventName')
#         data = {
#             'n1':n1
#         }
#         temp.eventName = request.POST.get('eventName')
#         temp.eventPlace = request.POST.get('eventPlace')
#         temp.eventDescription = request.POST.get('eventDescription')
#         temp.eventDate = request.POST.get("eventDate")
            
#         if len(request.FILES) != 0:
#             temp.eventImageOne = request.FILES['imgOne']
#             temp.eventImageTwo = request.FILES['imgTwo']
#             temp.eventImageThree = request.FILES['imgThree']

#         temp.save()
#         messages.success(request, "your data is added to database")
#         return HttpResponseRedirect('eventAdminApp/editAdmin.html', data)
#   n1 = request.POST['eventName']
#   n2 = request.POST['eventPlace']
#   member = 
#   member.n1 = eventName
#   member.lastname = last
#   member.save()
#   return HttpResponseRedirect(reverse('index'))




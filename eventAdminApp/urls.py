
from . import views
from django.urls import path

urlpatterns = [
    #admin Urls

    path('addClient/', views.saveDataAdmin, name='saveDataAdmin'),
    # path('<int:id>/', views.updateData, name='updateData'),
    path('DetailsAdmin/', views.editAdmin, name='editAdmin'),
    path('delete/<int:id>/', views.deleteData, name='deleteDataadmin'),
    path('deletev/<int:id>/', views.deleteVideo, name='deleteV'),
    path('vinput/', views.vInput, name='videoinput'),
    path('admin_login/', views.my_view, name='my_view'),


    
    #user Urls
    path('', views.hpServices, name='hpServices'),
    path('gallery/', views.galleryTemplate, name='galleryTemplate'),
    path('videos/', views.videoGallery, name='videoGalleryone'),
    path('contact/', views.hpEventContact, name='contactUs'),
    

]


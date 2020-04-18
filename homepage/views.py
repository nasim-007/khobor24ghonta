from django.shortcuts import render, redirect, get_object_or_404
from homepage.models import BreakingNews
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.db.models import Count
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.contrib.contenttypes.fields import GenericRelation
from django.utils import timezone
from video.models import VideoPost
from politics.models import PoliticsPost
from sport.models import SportPost, SportComment
from travel.models import TravelPost
from fashion.models import FashionPost
from health.models import HealthPost
from technology.models import TechnologyPost
from international.models import InternationalPost
from education.models import EducationPost
from funny.models import FunnyPost
from bangladesh.models import BangladeshPost
from homepage.models import Contact
from homepage.forms import ContactForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

import math





# Create your views here.
def homepage(request):
    
    bnews = BreakingNews.objects.filter(status=1).order_by('-created')
    
    paginator = Paginator(bnews, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    
    
    popular_sport_posts = SportPost.objects.filter(status=1).order_by('-created_on')[:1]
    popular_technology_posts = TechnologyPost.objects.filter(status=1).order_by('-created_on')[:1]
    popular_health_posts = HealthPost.objects.filter(status=1).order_by('-created_on')[:1]
    popular_fashion_posts = FashionPost.objects.filter(status=1).order_by('-created_on')[:1]
    
    
    most_view_politics_posts = PoliticsPost.objects.filter(status=1).order_by('-created_on')[:1]
    most_view_bangladesh_posts = BangladeshPost.objects.filter(status=1).order_by('-created_on')[:1]
    most_view_sport_posts = SportPost.objects.filter(status=1).order_by('-created_on')[:1]
    most_view_education_posts = EducationPost.objects.filter(status=1).order_by('-created_on')[:1]
    
    slide_view_international_posts = InternationalPost.objects.filter(status=1).order_by('-created_on')[:1]
    slide_view_funny_posts = FunnyPost.objects.filter(status=1).order_by('-created_on')[:1]
    slide_view_travel_posts = TravelPost.objects.filter(status=1).order_by('-created_on')[:1]

    videoposts = VideoPost.objects.filter(status=1).order_by('-created_on')[:3]
    
    sport_post_1 = SportPost.objects.filter(status=1).order_by('-created_on')[:1]
    travel_post_1 = TravelPost.objects.filter(status=1).order_by('-created_on')[:1]
    fashion_post_1 = FashionPost.objects.filter(status=1).order_by('-created_on')[:1]
    health_post_1 = HealthPost.objects.filter(status=1).order_by('-created_on')[:1]
    technology_post_1 = TechnologyPost.objects.filter(status=1).order_by('-created_on')[:1]
    
    international_post_recent_f2 = InternationalPost.objects.filter(status=1).order_by('-created_on')[:2]
    technology_post_recent_s1 = TechnologyPost.objects.filter(status=1).order_by('-created_on')[:1]
    education_post_recent = EducationPost.objects.filter(status=1).order_by('-created_on')[:1]
    funny_post_recent = FunnyPost.objects.filter(status=1).order_by('-created_on')[:1]
    health_post_recent = HealthPost.objects.filter(status=1).order_by('-created_on')[:1]
    
    bangladesh_post_latest = BangladeshPost.objects.filter(status=1).order_by('-created_on')[:1]
    health_post_latest = HealthPost.objects.filter(status=1).order_by('-created_on')[:1]
    education_post_latest = EducationPost.objects.filter(status=1).order_by('-created_on')[:1]
    funny_post_latest = FunnyPost.objects.filter(status=1).order_by('-created_on')[:1]
    fashion_post_latest = FashionPost.objects.filter(status=1).order_by('-created_on')[:1]
    
    politics_post_1 = PoliticsPost.objects.filter(status=1).order_by('-created_on')[:1]
    
    politics_post_2 = PoliticsPost.objects.filter(status=1).order_by('-created_on')[1:2]
    politics_post_3 = PoliticsPost.objects.filter(status=1).order_by('-created_on')[2:3]
    politics_post_4 = PoliticsPost.objects.filter(status=1).order_by('-created_on')[3:4]
    politics_post_5 = PoliticsPost.objects.filter(status=1).order_by('-created_on')[4:5]

    politics_post_6 = PoliticsPost.objects.filter(status=1).order_by('-created_on')[5:6]
    
    politics_post_7 = PoliticsPost.objects.filter(status=1).order_by('-created_on')[6:7]
    politics_post_8 = PoliticsPost.objects.filter(status=1).order_by('-created_on')[7:8]
    politics_post_9 = PoliticsPost.objects.filter(status=1).order_by('-created_on')[8:9]
    politics_post_10 = PoliticsPost.objects.filter(status=1).order_by('-created_on')[9:10]
    
    
    

    context = {
        "page_obj": page_obj,
        
        "popular_sport_posts": popular_sport_posts,
        "popular_technology_posts": popular_technology_posts,
        "popular_health_posts": popular_health_posts,
        "popular_fashion_posts": popular_fashion_posts,
        
        
        "most_view_politics_posts": most_view_politics_posts,
        "most_view_bangladesh_posts": most_view_bangladesh_posts,
        "most_view_sport_posts": most_view_sport_posts,
        "most_view_education_posts": most_view_education_posts,
        
        "slide_view_travel_posts": slide_view_travel_posts,
        "slide_view_international_posts": slide_view_international_posts,
        "slide_view_funny_posts": slide_view_funny_posts,
        
        "videoposts": videoposts,
        
        "sport_post_1": sport_post_1,
        "travel_post_1": travel_post_1,
        "fashion_post_1": fashion_post_1,
        "health_post_1": health_post_1,
        "technology_post_1": technology_post_1,
       
        "bangladesh_post_latest": bangladesh_post_latest,
        "health_post_latest": health_post_latest,
        "education_post_latest": education_post_latest,
        "funny_post_latest": funny_post_latest,
        "fashion_post_latest": fashion_post_latest,
        
        "international_post_recent_f2": international_post_recent_f2,
        "technology_post_recent_s1": technology_post_recent_s1,
        "education_post_recent": education_post_recent, 
        "funny_post_recent": funny_post_recent,
        "health_post_recent": health_post_recent,
        
        
        "politics_post_1": politics_post_1,
        "politics_post_2": politics_post_2,
        "politics_post_3": politics_post_3,
        "politics_post_4": politics_post_4,
        "politics_post_5": politics_post_5,
        "politics_post_6": politics_post_6,
        "politics_post_7": politics_post_7,
        "politics_post_8": politics_post_8,
        "politics_post_9": politics_post_9,
        "politics_post_10": politics_post_10,
       
        
        
       

    }
    
    
    return render(request, 'homepage.html', context)


def contact(request):

    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            
            messages.success(request, 'আপনার ফর্মটি সফলভাবে জমা হয়েছে!', extra_tags='alert')
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('contact',))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
    
    
    
    context = {

      "form": form

    }
    
    return render(request, 'contact.html', context)
    
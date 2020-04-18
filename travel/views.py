
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from travel.models import TravelPost, TravelComment
from .forms import TravelCommentFrom
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.db.models import Count
from django.contrib import messages

# Create your views here.

def travel_index(request):
    
    travel_post_all = TravelPost.objects.filter(status=1).order_by('-created_on')
    
    most_view_travel_posts = TravelPost.objects.filter(status=1).order_by('-created_on')[4:8]
    
    popular_travel_posts = TravelPost.objects.filter(status=1).order_by('-created_on')[:4]
    
    
    
    paginator = Paginator(travel_post_all, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'most_view_travel_posts': most_view_travel_posts,
        'popular_travel_posts': popular_travel_posts,
        
    }
    return render(request, "travel_index.html", context)



def travel_detail(request, pk):
    
    
    travelpost = TravelPost.objects.get(pk=pk)
    
    

    travel_slide_post = TravelPost.objects.filter(status=1).order_by('-created_on')[:3]
    
    travel_post_related_s3 = TravelPost.objects.filter(status=1).order_by('-created_on')[:3]
    
    travel_post_related_s6 = TravelPost.objects.filter(status=1).order_by('-created_on')[3:6]
    
    
    
   
    
    most_view_travel_posts = TravelPost.objects.filter(status=1).order_by('-created_on')[4:8]
    
    popular_travel_posts = TravelPost.objects.filter(status=1).order_by('-created_on')[:4]
    
    travelpost.visit_travel += 1
    travelpost.save()
    
    comments = travelpost.travel_comments.filter(active=True, parent__isnull=True).order_by('-created')
    
    commentslatest = travelpost.travel_comments.filter(active=True, parent__isnull=True).order_by('-created')[:2]
    
    if request.method == 'POST':
        # comment has been added
        comment_form =TravelCommentFrom(data=request.POST)
        if comment_form.is_valid():
            parent_obj = None
            # get parent comment id from hidden input
            try:
                # id integer e.g. 15
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            # if parent_id has been submitted get parent_obj id
            if parent_id:
                parent_obj = TravelComment.objects.get(id=parent_id)
                # if parent object exist
                if parent_obj:
                    # create replay comment object
                    replay_comment = comment_form.save(commit=False)
                    # assign parent_obj to replay comment
                    replay_comment.parent = parent_obj
            # normal comment
            # create comment object but do not save to database
            new_comment = comment_form.save(commit=False)
            # assign ship to the comment
            new_comment.travelpost = travelpost
            # save
            new_comment.save()
            messages.success(request, 'আপনার মন্তব্য সফলভাবে জমা হয়েছে!', extra_tags='alert')
            return HttpResponseRedirect(reverse('travel_detail', args=(travelpost.pk,)))
    else:
        comment_form = TravelCommentFrom()
    
    
    
    
    context = {
        
        "travelpost": travelpost,

        "travel_slide_post": travel_slide_post,
        "travel_post_related_s3": travel_post_related_s3,
        "travel_post_related_s6": travel_post_related_s6,
        
        
        "most_view_travel_posts": most_view_travel_posts,
        "popular_travel_posts": popular_travel_posts,
        
       
        "comments": comments,
        "commentslatest": commentslatest,
        "comment_form": comment_form,
        "count_hit": count_hit
       
      
    }

    return render(request, "travel_detail.html", context)


def search_travel(request):
    queryset = TravelPost.objects.filter(status=1).order_by('-created_on')
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(travel_title__icontains=query) |
            Q(travel_content__icontains=query)
           
        
        ).distinct()
    context = {
        'queryset': queryset,
       

    }
    return render(request, 'search_travel.html', context)




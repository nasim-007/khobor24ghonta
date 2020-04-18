from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from technology.models import TechnologyPost, TechnologyComment
from .forms import TechnologyCommentFrom
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.db.models import Count
from django.contrib import messages

# Create your views here.

def technology_index(request):
    
    technology_post_all = TechnologyPost.objects.filter(status=1).order_by('-created_on')
    
    most_view_technology_posts = TechnologyPost.objects.filter(status=1).order_by('-created_on')[4:8]
    
    popular_technology_posts = TechnologyPost.objects.filter(status=1).order_by('-created_on')[:4]
    
    technology_post_feature = TechnologyPost.objects.filter(status=2).order_by('-created_on')[:1]
    
    paginator = Paginator(technology_post_all, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'most_view_technology_posts': most_view_technology_posts,
        'popular_technology_posts': popular_technology_posts,
        'technology_post_feature': technology_post_feature
    }
    return render(request, "technology_index.html", context)



def technology_detail(request, pk):
    
    
    technologypost = TechnologyPost.objects.get(pk=pk)
    
    

    technology_slide_post = TechnologyPost.objects.filter(status=1).order_by('-created_on')[:3]
    
    technology_post_related_s3 = TechnologyPost.objects.filter(status=1).order_by('-created_on')[:3]
    
    technology_post_related_s6 = TechnologyPost.objects.filter(status=1).order_by('-created_on')[3:6]
    
    
    
   
    
    most_view_technology_posts = TechnologyPost.objects.filter(status=1).order_by('-created_on')[4:8]
    
    popular_technology_posts = TechnologyPost.objects.filter(status=1).order_by('-created_on')[:4]
    
    technologypost.visit_technology += 1
    technologypost.save()
    
    comments = technologypost.technology_comments.filter(active=True, parent__isnull=True).order_by('-created')
    
    commentslatest = technologypost.technology_comments.filter(active=True, parent__isnull=True).order_by('-created')[:2]
    
    if request.method == 'POST':
        # comment has been added
        comment_form = TechnologyCommentFrom(data=request.POST)
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
                parent_obj = TechnologyComment.objects.get(id=parent_id)
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
            new_comment.technologypost = technologypost
            # save
            new_comment.save()
            messages.success(request, 'আপনার মন্তব্য সফলভাবে জমা হয়েছে!', extra_tags='alert')
            return HttpResponseRedirect(reverse('technology_detail', args=(technologypost.pk,)))
    else:
        comment_form = TechnologyCommentFrom()
    
    
    
    
    context = {
        
        "technologypost": technologypost,

        "technology_slide_post": technology_slide_post,
        "technology_post_related_s3": technology_post_related_s3,
        "technology_post_related_s6": technology_post_related_s6,
        
        
        "most_view_technology_posts": most_view_technology_posts,
        "popular_technology_posts": popular_technology_posts,
        
       
        "comments": comments,
        "commentslatest": commentslatest,
        "comment_form": comment_form,
       
       
      
    }

    return render(request, "technology_detail.html", context)



def search_technology(request):
    queryset = TechnologyPost.objects.filter(status=1).order_by('-created_on')
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(technology_title__icontains=query) |
            Q(technology_content__icontains=query)
           
        
        ).distinct()
    context = {
        'queryset': queryset,
       

    }
    return render(request, 'search_technology.html', context)


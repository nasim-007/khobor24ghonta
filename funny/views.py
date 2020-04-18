
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from funny.models import FunnyPost, FunnyComment
from fashion.models import FashionPost
from .forms import FunnyCommentFrom
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.db.models import Count
from django.contrib import messages

# Create your views here.

def funny_index(request):
    
    funny_post_all = FunnyPost.objects.filter(status=1).order_by('-created_on')
    
    most_view_funny_posts = FunnyPost.objects.filter(status=1).order_by('-created_on')[4:8]
    
    popular_funny_posts = FunnyPost.objects.filter(status=1).order_by('-created_on')[:4]
    
    
    
    paginator = Paginator(funny_post_all, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'most_view_funny_posts': most_view_funny_posts,
        'popular_funny_posts': popular_funny_posts,
        
    }
    return render(request, "funny_index.html", context)



def funny_detail(request, pk):
    
    
    funnypost = FunnyPost.objects.get(pk=pk)
    
    

    funny_slide_post = FunnyPost.objects.filter(status=1).order_by('-created_on')[:3]
    
    funny_post_related_s3 = FunnyPost.objects.filter(status=1).order_by('-created_on')[:3]
    
    funny_post_related_s6 = FunnyPost.objects.filter(status=1).order_by('-created_on')[3:6]
    
    
    
   
    
    most_view_funny_posts = FunnyPost.objects.filter(status=1).order_by('-created_on')[4:8]
    
    popular_funny_posts = FunnyPost.objects.filter(status=1).order_by('-created_on')[:4]
    
    funnypost.visit_funny += 1
    funnypost.save()
    
    comments = funnypost.funny_comments.filter(active=True, parent__isnull=True).order_by('-created')
    
    commentslatest = funnypost.funny_comments.filter(active=True, parent__isnull=True).order_by('-created')[:2]
    
    if request.method == 'POST':
        # comment has been added
        comment_form = FunnyCommentFrom(data=request.POST)
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
                parent_obj = FunnyComment.objects.get(id=parent_id)
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
            new_comment.funnypost = funnypost
            # save
            new_comment.save()
            messages.success(request, 'আপনার মন্তব্য সফলভাবে জমা হয়েছে!', extra_tags='alert')
            return HttpResponseRedirect(reverse('funny_detail', args=(funnypost.pk,)))
    else:
        comment_form = FunnyCommentFrom()
    
    
    
    
    context = {
        
        "funnypost": funnypost,

        "funny_slide_post": funny_slide_post,
        "funny_post_related_s3": funny_post_related_s3,
        "funny_post_related_s6": funny_post_related_s6,
        
        
        "most_view_funny_posts": most_view_funny_posts,
        "popular_funny_posts": popular_funny_posts,
        
       
        "comments": comments,
        "commentslatest": commentslatest,
        "comment_form": comment_form,
        "count_hit": count_hit
       
      
    }

    return render(request, "funny_detail.html", context)

def search_funny(request):
    queryset = FunnyPost.objects.filter(status=1).order_by('-created_on')
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(funny_title__icontains=query) |
            Q(funny_content__icontains=query)
           
        
        ).distinct()
    context = {
        'queryset': queryset,
       

    }
    return render(request, 'search_funny.html', context)




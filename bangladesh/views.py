

from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from bangladesh.models import BangladeshPost, BangladeshComment
from .forms import BangladeshCommentFrom
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.db.models import Count
from django.contrib import messages

# Create your views here.

def bangladesh_index(request):
    
    bangladesh_post_all = BangladeshPost.objects.filter(status=1).order_by('-created_on')
    
    most_view_bangladesh_posts = BangladeshPost.objects.filter(status=1).order_by('-created_on')[4:8]
    
    popular_bangladesh_posts = BangladeshPost.objects.filter(status=1).order_by('-created_on')[:4]
    
    
    
    paginator = Paginator(bangladesh_post_all, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'most_view_bangladesh_posts': most_view_bangladesh_posts,
        'popular_bangladesh_posts': popular_bangladesh_posts,
        
    }
    return render(request, "bangladesh_index.html", context)



def bangladesh_detail(request, pk):
    
    
    bangladeshpost = BangladeshPost.objects.get(pk=pk)
    
    

    bangladesh_slide_post = BangladeshPost.objects.filter(status=1).order_by('-created_on')[:3]
    
    bangladesh_post_related_s3 = BangladeshPost.objects.filter(status=1).order_by('-created_on')[:3]
    
    bangladesh_post_related_s6 = BangladeshPost.objects.filter(status=1).order_by('-created_on')[3:6]
    
    
    
   
    
    most_view_bangladesh_posts = BangladeshPost.objects.filter(status=1).order_by('-created_on')[4:8]
    
    popular_bangladesh_posts = BangladeshPost.objects.filter(status=1).order_by('-created_on')[:4]
    
    bangladeshpost.visit_bangladesh += 1
    bangladeshpost.save()
    
    comments = bangladeshpost.bangladesh_comments.filter(active=True, parent__isnull=True).order_by('-created')
    
    commentslatest = bangladeshpost.bangladesh_comments.filter(active=True, parent__isnull=True).order_by('-created')[:2]
    
    if request.method == 'POST':
        # comment has been added
        comment_form = BangladeshCommentFrom(data=request.POST)
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
                parent_obj = BangladeshComment.objects.get(id=parent_id)
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
            new_comment.bangladeshpost = bangladeshpost
            # save
            new_comment.save()
            messages.success(request, 'আপনার মন্তব্য সফলভাবে জমা হয়েছে!', extra_tags='alert')
            
            return HttpResponseRedirect(reverse('bangladesh_detail', args=(bangladeshpost.pk,)))
    else:
        comment_form = BangladeshCommentFrom()
    
    
    
    
    context = {
        
        "bangladeshpost": bangladeshpost,

        "bangladesh_slide_post": bangladesh_slide_post,
        "bangladesh_post_related_s3": bangladesh_post_related_s3,
        "bangladesh_post_related_s6": bangladesh_post_related_s6,
        
        
        "most_view_bangladesh_posts": most_view_bangladesh_posts,
        "popular_bangladesh_posts": popular_bangladesh_posts,
        
       
        "comments": comments,
        "commentslatest": commentslatest,
        "comment_form": comment_form,
       
       
      
    }

    return render(request, "bangladesh_detail.html", context)




def search_bangladesh(request):
    queryset = BangladeshPost.objects.filter(status=1).order_by('-created_on')
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(bangladesh_title__icontains=query) |
            Q(bangladesh_content__icontains=query)
           
        
        ).distinct()
    context = {
        'queryset': queryset,
       

    }
    return render(request, 'search_bangladesh.html', context)


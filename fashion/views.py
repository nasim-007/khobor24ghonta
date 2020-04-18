
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from fashion.models import FashionPost, FashionComment
from .forms import FashionCommentFrom
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.db.models import Count
from django.contrib import messages

# Create your views here.

def fashion_index(request):
    
    fashion_post_all = FashionPost.objects.filter(status=1).order_by('-created_on')
    
    most_view_fashion_posts = FashionPost.objects.filter(status=1).order_by('-created_on')[4:8]
    
    popular_fashion_posts = FashionPost.objects.filter(status=1).order_by('-created_on')[:4]
    
    
    
    paginator = Paginator(fashion_post_all, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'most_view_fashion_posts': most_view_fashion_posts,
        'popular_fashion_posts': popular_fashion_posts,
        
    }
    return render(request, "fashion_index.html", context)



def fashion_detail(request, pk):
    
    
    fashionpost = FashionPost.objects.get(pk=pk)
    
    

    fashion_slide_post = FashionPost.objects.filter(status=1).order_by('-created_on')[:3]
    
    fashion_post_related_s3 = FashionPost.objects.filter(status=1).order_by('-created_on')[:3]
    
    fashion_post_related_s6 = FashionPost.objects.filter(status=1).order_by('-created_on')[3:6]
    
    
    
   
    
    most_view_fashion_posts = FashionPost.objects.filter(status=1).order_by('-created_on')[4:8]
    
    popular_fashion_posts = FashionPost.objects.filter(status=1).order_by('-created_on')[:4]
    
    fashionpost.visit_fashion += 1
    fashionpost.save()
    
    comments = fashionpost.fashion_comments.filter(active=True, parent__isnull=True).order_by('-created')
    
    commentslatest = fashionpost.fashion_comments.filter(active=True, parent__isnull=True).order_by('-created')[:2]
    
    if request.method == 'POST':
        # comment has been added
        comment_form = FashionCommentFrom(data=request.POST)
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
                parent_obj = FashionComment.objects.get(id=parent_id)
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
            new_comment.fashionpost = fashionpost
            # save
            new_comment.save()
            messages.success(request, 'আপনার মন্তব্য সফলভাবে জমা হয়েছে!', extra_tags='alert')
            return HttpResponseRedirect(reverse('fashion_detail', args=(fashionpost.pk,)))
    else:
        comment_form = FashionCommentFrom()
    
    
    
    
    context = {
        
        "fashionpost": fashionpost,

        "fashion_slide_post": fashion_slide_post,
        "fashion_post_related_s3": fashion_post_related_s3,
        "fashion_post_related_s6": fashion_post_related_s6,
        
        
        "most_view_fashion_posts": most_view_fashion_posts,
        "popular_fashion_posts": popular_fashion_posts,
        
       
        "comments": comments,
        "commentslatest": commentslatest,
        "comment_form": comment_form,
        "count_hit": count_hit
       
      
    }

    return render(request, "fashion_detail.html", context)


def search_fashion(request):
    queryset = FashionPost.objects.filter(status=1).order_by('-created_on')
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(fashion_title__icontains=query) |
            Q(fashion_content__icontains=query)
           
        
        ).distinct()
    context = {
        'queryset': queryset,
       

    }
    return render(request, 'search_fashion.html', context)



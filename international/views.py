
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from international.models import InternationalPost, InternationalComment
from .forms import InternationalCommentFrom
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.db.models import Count
from django.contrib import messages

# Create your views here.

def international_index(request):
    
    international_post_all = InternationalPost.objects.filter(status=1).order_by('-created_on')
    
    most_view_international_posts = InternationalPost.objects.filter(status=1).order_by('-created_on')[4:8]
    
    popular_international_posts = InternationalPost.objects.filter(status=1).order_by('-created_on')[:4]
    
    
    
    paginator = Paginator(international_post_all, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'most_view_international_posts': most_view_international_posts,
        'popular_international_posts': popular_international_posts,
        
    }
    return render(request, "international_index.html", context)



def international_detail(request, pk):
    
    
    internationalpost = InternationalPost.objects.get(pk=pk)
    
    

    international_slide_post = InternationalPost.objects.filter(status=1).order_by('-created_on')[:3]
    
    international_post_related_s3 = InternationalPost.objects.filter(status=1).order_by('-created_on')[:3]
    
    international_post_related_s6 = InternationalPost.objects.filter(status=1).order_by('-created_on')[3:6]
    
    
    
   
    
    most_view_international_posts = InternationalPost.objects.filter(status=1).order_by('-created_on')[4:8]
    
    popular_international_posts = InternationalPost.objects.filter(status=1).order_by('-created_on')[:4]
    
    internationalpost.visit_international += 1
    internationalpost.save()
    
    comments = internationalpost.international_comments.filter(active=True, parent__isnull=True).order_by('-created')
    
    commentslatest = internationalpost.international_comments.filter(active=True, parent__isnull=True).order_by('-created')[:2]
    
    if request.method == 'POST':
        # comment has been added
        comment_form = InternationalCommentFrom(data=request.POST)
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
                parent_obj = InternationalComment.objects.get(id=parent_id)
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
            new_comment.internationalpost = internationalpost
            # save
            new_comment.save()
            messages.success(request, 'আপনার মন্তব্য সফলভাবে জমা হয়েছে!', extra_tags='alert')
            return HttpResponseRedirect(reverse('international_detail', args=(internationalpost.pk,)))
    else:
        comment_form = InternationalCommentFrom()
    
    
    
    
    context = {
        
        "internationalpost": internationalpost,

        "international_slide_post": international_slide_post,
        "international_post_related_s3": international_post_related_s3,
        "international_post_related_s6": international_post_related_s6,
        
        
        "most_view_international_posts": most_view_international_posts,
        "popular_international_posts": popular_international_posts,
        
       
        "comments": comments,
        "commentslatest": commentslatest,
        "comment_form": comment_form,
        "count_hit": count_hit
       
      
    }

    return render(request, "international_detail.html", context)





def search_international(request):
    queryset = InternationalPost.objects.filter(status=1).order_by('-created_on')
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(international_title__icontains=query) |
            Q(international_content__icontains=query)
           
        
        ).distinct()
    context = {
        'queryset': queryset,
       

    }
    return render(request, 'search_international.html', context)
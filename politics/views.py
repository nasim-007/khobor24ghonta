from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from politics.models import PoliticsPost, PoliticsComment
from .forms import PoliticsCommentFrom
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.db.models import Count
from django.contrib import messages

# Create your views here.

def politics_index(request):
    
    politics_post_all = PoliticsPost.objects.filter(status=1).order_by('-created_on')
    
    popular_politics_posts = PoliticsPost.objects.filter(status=1).order_by('-created_on')[:4]
    most_view_politics_posts = PoliticsPost.objects.filter(status=1).order_by('-created_on')[4:8]
    
    paginator = Paginator(politics_post_all, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'popular_politics_posts': popular_politics_posts,
        'most_view_politics_posts': most_view_politics_posts
    }
    return render(request, "politics_index.html", context)



def politics_detail(request, pk):
    
    
    politicspost = PoliticsPost.objects.get(pk=pk)
    
    

    politics_slide_post = PoliticsPost.objects.filter(status=1).order_by('-created_on')[:3]
    
    politics_post_related_s3 = PoliticsPost.objects.filter(status=1).order_by('-created_on')[:3]
    
    politics_post_related_s6 = PoliticsPost.objects.filter(status=1).order_by('-created_on')[3:6]
    
    
    
    popular_politics_posts = PoliticsPost.objects.filter(status=1).order_by('-created_on')[:4]
    
    most_view_politics_posts = PoliticsPost.objects.filter(status=1).order_by('-created_on')[4:8]
    
    politicspost.visit_politics += 1
    politicspost.save()
    
    comments = politicspost.politics_comments.filter(active=True, parent__isnull=True).order_by('-created')
    
    commentslatest = politicspost.politics_comments.filter(active=True, parent__isnull=True).order_by('-created')[:2]
    
    if request.method == 'POST':
        # comment has been added
        comment_form = PoliticsCommentFrom(data=request.POST)
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
                parent_obj = PoliticsComment.objects.get(id=parent_id)
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
            new_comment.politicspost = politicspost
            # save
            new_comment.save()
            messages.success(request, 'আপনার মন্তব্য সফলভাবে জমা হয়েছে!', extra_tags='alert')
            return HttpResponseRedirect(reverse('politics_detail', args=(politicspost.pk,)))
    else:
        comment_form = PoliticsCommentFrom()
    
    
    
    
    context = {
        
        "politicspost": politicspost,

        "politics_slide_post": politics_slide_post,
        "politics_post_related_s3": politics_post_related_s3,
        "politics_post_related_s6": politics_post_related_s6,
        
        
        "most_view_politics_posts": most_view_politics_posts,
        "popular_politics_posts": popular_politics_posts,
        
       
        "comments": comments,
        "commentslatest": commentslatest,
        "comment_form": comment_form,
      
       
      
    }

    return render(request, "politics_detail.html", context)


def search_politics(request):
    queryset = PoliticsPost.objects.filter(status=1).order_by('-created_on')
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(politics_title__icontains=query) |
            Q(politics_content__icontains=query)
           
        
        ).distinct()
    context = {
        'queryset': queryset,
       

    }
    return render(request, 'search_politics.html', context)

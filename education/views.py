
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from education.models import EducationPost, EducationComment
from .forms import EducationCommentFrom
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.db.models import Count
from django.contrib import messages


# Create your views here.

def education_index(request):
    
    education_post_all = EducationPost.objects.filter(status=1).order_by('-created_on')
    
    most_view_education_posts = EducationPost.objects.filter(status=1).order_by('-created_on')[4:8]
    
    popular_education_posts = EducationPost.objects.filter(status=1).order_by('-created_on')[:4]
    
    
    
    paginator = Paginator(education_post_all, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'most_view_education_posts': most_view_education_posts,
        'popular_education_posts': popular_education_posts,
        
    }
    return render(request, "education_index.html", context)



def education_detail(request, pk):
    
    
    educationpost = EducationPost.objects.get(pk=pk)
    
    

    education_slide_post = EducationPost.objects.filter(status=1).order_by('-created_on')[:3]
    
    education_post_related_s3 = EducationPost.objects.filter(status=1).order_by('-created_on')[:3]
    
    education_post_related_s6 = EducationPost.objects.filter(status=1).order_by('-created_on')[3:6]
    
    
    
   
    
    most_view_education_posts = EducationPost.objects.filter(status=1).order_by('-created_on')[4:8]
    
    popular_education_posts = EducationPost.objects.filter(status=1).order_by('-created_on')[:4]
    
    educationpost.visit_education += 1
    educationpost.save()
    
    comments = educationpost.education_comments.filter(active=True, parent__isnull=True).order_by('-created')
    
    commentslatest = educationpost.education_comments.filter(active=True, parent__isnull=True).order_by('-created')[:2]
    
    if request.method == 'POST':
        # comment has been added
        comment_form = EducationCommentFrom(data=request.POST)
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
                parent_obj = EducationComment.objects.get(id=parent_id)
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
            new_comment.educationpost = educationpost
            # save
            new_comment.save()
            messages.success(request, 'আপনার মন্তব্য সফলভাবে জমা হয়েছে!', extra_tags='alert')
            
            return HttpResponseRedirect(reverse('education_detail', args=(educationpost.pk,)))
    else:
        comment_form = EducationCommentFrom()
    
    
    
    
    context = {
        
        "educationpost": educationpost,

        "education_slide_post": education_slide_post,
        "education_post_related_s3": education_post_related_s3,
        "education_post_related_s6": education_post_related_s6,
        
        
        "most_view_education_posts": most_view_education_posts,
        "popular_education_posts": popular_education_posts,
        
       
        "comments": comments,
        "commentslatest": commentslatest,
        "comment_form": comment_form,
        "count_hit": count_hit
       
      
    }

    return render(request, "education_detail.html", context)




def search_education(request):
    queryset = EducationPost.objects.filter(status=1).order_by('-created_on')
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(education_title__icontains=query) |
            Q(education_content__icontains=query)
           
        
        ).distinct()
    context = {
        'queryset': queryset,
       

    }
    return render(request, 'search_education.html', context)

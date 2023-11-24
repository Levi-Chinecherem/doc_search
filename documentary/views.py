import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Documentary, Comment, Reply
from .forms import CommentForm, ReplyForm, DocumentaryForm
from django.contrib.auth.decorators import login_required
from django.db import models
from django.db.models import Q

def home(request):
    return render(request, 'home.html')

@login_required
def documentary_list(request):
    query = request.GET.get('q')
    
    if query:
        # Perform a search across multiple fields using Q objects
        documentaries = Documentary.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(author__icontains=query) |
            Q(year__icontains=query)  # Assuming year is an integer field
        )
    else:
        documentaries = Documentary.objects.all()

    context = {'documentaries': documentaries, 'query': query}
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render(request, 'documentary/documentary_list_ajax.html', context)

    return render(request, 'documentary/documentary_list.html', context)

@login_required
def documentary_details(request, documentary_id):
    documentary = get_object_or_404(Documentary, pk=documentary_id)
    comments = documentary.comments.all()

    if request.method == 'POST':
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                # Save the comment
                comment = comment_form.save(commit=False)
                comment.documentary = documentary
                comment.user = request.user
                comment.save()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'errors': comment_form.errors})
        else:
            comment_form = CommentForm(request.POST)
            reply_form = ReplyForm()

            if comment_form.is_valid():
                # Save the comment
                comment = comment_form.save(commit=False)
                comment.documentary = documentary
                comment.user = request.user
                comment.save()
                return redirect('documentary_details', pk=pk)
    else:
        comment_form = CommentForm()
        reply_form = ReplyForm()

    context = {
        'documentary': documentary,
        'comments': comments,
        'comment_form': comment_form,
        'reply_form': reply_form,
    }
    return render(request, 'documentary/documentary_details.html', context)

@login_required
def register_documentary(request):
    if request.method == 'POST':
        form = DocumentaryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Documentary added successfully'})
        else:
            return JsonResponse({'success': False, 'message': 'Failed to add documentary'})
    else:
        form = DocumentaryForm()
    return render(request, 'documentary/register_documentary.html', {'form': form})

@login_required
def submit_comment(request, documentary_id):
    documentary = get_object_or_404(Documentary, id=documentary_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.documentary = documentary
            comment.user = request.user
            comment.save()
            return JsonResponse({'status': 'success', 'comment_id': comment.id})
    return JsonResponse({'status': 'error'})

@login_required
def documentary_registered(request):
    if request.method == 'POST':
        form = DocumentaryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Documentary added successfully'})
        else:
            return JsonResponse({'success': False, 'message': 'Failed to add documentary'})
    else:
        form = DocumentaryForm()
    return render(request, 'documentary/register_documentary.html', {'form': form})


@login_required
def submit_reply(request, documentary_id):
    comment_id = request.POST.get('comment_id')
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.comment = comment
            reply.user = request.user
            reply.save()
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})


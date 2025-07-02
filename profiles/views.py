from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ReviewForm
from .models import Review


def profiles(request):
    """ A view to return the index page """

    return render(request, 'profiles.html')


def review_list(request):
    """ view to create list of current user reviews """
    reviews = Review.objects.filter(user=request.user)
    return render(request, 'review_list.html', {'reviews': reviews})


def review_create(request):
    """ view to create a new review """
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        review = form.save(commit=False)
        review.user = request.user
        review.save()
        messages.success(request, "Review submitted.")
        return redirect('profiles:review_list')
    else:
        messages.error(request, "There was an error with your submission.")
    return render(request, 'review_form.html', {'form': form})


def review_update(request, pk):
    """ view to edit an existing review """
    review = get_object_or_404(Review, pk=pk, user=request.user)
    form = ReviewForm(request.POST or None, instance=review)
    if form.is_valid():
        form.save()
        return redirect('profiles:review_list')
    return render(request, 'review_form.html', {'form': form})


def review_delete(request, pk):
    """ view to delete a reveiw """
    review = get_object_or_404(Review, pk=pk, user=request.user)
    if request.method == 'POST':
        review.delete()
        return redirect('profiles:review_list')
    return render(request, 'profiles:review_list', {'review': review})
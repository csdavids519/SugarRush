from django.shortcuts import render, get_object_or_404, redirect
from profiles.models import Customer
from .models import Review
from .forms import ReviewForm


def profiles(request):
    """ A view to return the index page """

    return render(request, 'profiles.html')


def order_history(request):
    """ A view to return the index page """
    try:
        orders = Customer.objects.get(user=request.user)
    except Customer.DoesNotExist:
        return render(request, 'order_history.html', {'order_results': None})
    return render(request, 'order_history.html', {'order_results': orders})


def review_list(request):
    """ view to create list of current user reviews """
    reviews = Review.objects.all()
    return render(request, 'review_list.html', {'reviews': reviews})


def review_create(request):
    """ view to create a new review """
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        review = form.save(commit=False)
        review.user = request.user
        review.save()
        return redirect('profiles:review_list')
    return render(request, 'review_form.html', {'form': form})


def review_update(request, pk):
    """ view to edit an existing review """
    review = get_object_or_404(Review, pk=pk, user=request.user)
    form = ReviewForm(request.POST or None, instance=review)
    print("Review:", review.pk)
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
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import timezone


from .models import Book, Author, BookCheckout


@login_required
def index(request):
    user = request.user

    if request.method == 'POST':
        if 'book_id' in request.POST:
            book_id = request.POST['book_id']
            checkout = BookCheckout(user=user, book_id=book_id)
            checkout.save()
        else:
            checkout_id = request.POST['checkout_id']
            checkout = BookCheckout.objects.get(pk=checkout_id)
            checkout.checkin_date = timezone.now()
            checkout.save()

    # find the books for which there is no associated bookcheckout where the checkindate is null
    books = Book.objects.all()
    available_books = []
    for book in books:
        # NOT THE SAME if book.checkouts.filter(checkin_date__isnull=False).exists():
        # there is no bookcheckout for which the checkin_date is null
        if not book.checkouts.filter(checkin_date__isnull=True).exists():
            available_books.append(book)
    active_checkouts = user.checkouts.filter(checkin_date__isnull=True)

    inactive_checkouts = user.checkouts.filter(checkin_date__isnull=False)

    return render(request, 'library/index.html', {'available_books': available_books,
                                                  'active_checkouts': active_checkouts,
                                                  'inactive_checkouts': inactive_checkouts})

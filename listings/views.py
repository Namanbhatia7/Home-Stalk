from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from .models import Listing
from .choices import price_choices, bedroom_choices, state_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings,3)
    page = request.GET.get('page')
    paged_listing = paginator.get_page(page)

    context = {
        'listings': paged_listing
    }

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing' : listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):

    queryset_list = Listing.objects.order_by('-list_date')

    context = {
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'listings': queryset_list
    }
    
    return render(request, 'listings/search.html', context)

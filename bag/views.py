from django.shortcuts import render

# Create your views here.

def BagView(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')
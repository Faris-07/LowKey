from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse

# Create your views here.

def bag_view(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a chosen quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)

def adjust_bag(request, item_id):
    """ Adjust item's quantity in bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity') or 1)
    bag = request.session.get('bag', {})

    if quantity > 99:
        messages.error(
            request, 'Sorry, value must be less then or equal to 99.')
    elif quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Removes item from bag """
    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})
    bag.pop(item_id)
    messages.success(request, f'Removed {product.name} from your bag')
    request.session['bag'] = bag
    return HttpResponse(status=200)
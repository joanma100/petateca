from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from core.decorators import render_to

from serie.models import Serie
from book.models import Book
from userdata.models import User

@render_to('registration/profile.html')
@login_required
def view_profile(request):
    ''' TODO: Para cambiar cosas del perfil ''' 
    user_profile = request.user.get_profile()
    return { 'profile': user_profile, } 


@render_to('userdata/public_profile.html')
def public_profile(request, user_name):
    ''' Perfil publico del usuario ''' 
    user = get_object_or_404(User, username=user_name)
    # for series marked as favorite
    favorite_series = Serie.objects.select_related("poster").filter(favorite_of=user)
    # for books marked as favorite
    favorite_books = Book.objects.select_related("poster").filter(favorite_book=user)
    # comments for series
    serie = ContentType.objects.get(app_label='serie', name='serie')
    comments_series = user.comment_comments.filter(content_type=serie.id).order_by('-submit_date')[:10]
    return {
        'user': user,
        'favorite_series': favorite_series,
        'favorite_books': favorite_books,
        'comments_serie': comments_series,
    }


@render_to('userdata/activation_by_code.html')
def activate_by_code(request):
    if request.POST.get('activation_key'):
        activation_key = request.POST.get('activation_key')
        final_url = reverse('registration.views.activate', kwargs={
            'activation_key': activation_key
        })
        return HttpResponseRedirect(final_url)
    else: 
        return {'mensaje': 'Error'}


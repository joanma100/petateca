# pylint: disable-msg=W0401,W0614
from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_detail
from serie.models import Actor

get_actor = {
    'template_name': 'serie/get_actor.html',
    'template_object_name': 'actor',
    'queryset': Actor.objects.select_related('poster').all(),
    'slug_field': 'slug_name',
}


urlpatterns = patterns('serie.views',
    url(r'^actor/(?P<slug>[-\w]+)/$', object_detail, get_actor, name="get_actor"),
    url(r'^sneak/$', 'sneak_links', name="sneak_links"),
    url(r'^add/$', 'add_or_edit_serie', name="add_serie"),
    (r'^recommended/$', 'list_user_recommendation'),
)

urlpatterns += patterns('serie.ajax',
    # AJAX /series
    url(r'^$', 'serie_index', name='serie_index'), 
    url(r'^lookup/letter/(?P<letter>[-\w]+)/$', 'serie_index'),
    url(r'^lookup/genre/(?P<genre_slug>[-\w]+)/$', 'serie_index'),
    url(r'^lookup/network/(?P<network_slug>[-\w]+)/$', 'serie_index'),

    url(r'^lookup/serie/(?P<serie_id>[-\w]+)/$', 'serie_lookup'),
    url(r'^lookup/serie/(?P<serie_id>[-\w]+)/season/(?P<season>\d+)/$', 'season_lookup'),
    url(r'^lookup/actors/(?P<serie_slug>[-\w]+)/$', 'actors_lookup'),

    # AJAX /serie/nombre
    # - mostrar espoiler para episodio
    url(r'^lookup/espoiler/(?P<serie_id>[-\w]+)/(?P<season>\d+)/(?P<episode>\d+)/$', 'espoiler_lookup', name='ajax_espoiler'),

    # -tratar votaciones de los links
    url(r'^links/vote/(?P<link_type>[-\w]+)/$', 'vote_link', name='vote_link'),

    # - listar links de episodios y temporada
    url(r'^links/list/(?P<serie_id>[-\w]+)/season/(?P<season>\d+)/$', 'ajax_links_list', name='ajax_list_links_season'),
    url(r'^links/list/(?P<serie_id>[-\w]+)/(?P<season>\d+)/(?P<episode>\d+)/$', 'ajax_links_list', name='ajax_list_links_episodes'),

    # - agregar links de episodios y temporada
    url(r'^links/add/(?P<link_type>[-\w]+)/(?P<obj_id>\d+)/$', 'ajax_add_link', name='ajax_add_link'),

    # - agregar episodio 
    url(r'^lookup/serie/(?P<serie_id>\d+)/season/(?P<season>\d+)/add/episode/$', 'ajax_add_episode', name="ajax_add_episode"),
    # - editar episodio (descripcion e imagen)
    url(r'^lookup/serie/(?P<serie_id>\d+)/season/(?P<season>\d+)/edit/episode/(?P<episode>\d+)/$', 'ajax_edit_episode_description', name="ajax_edit_episode_description"),

)

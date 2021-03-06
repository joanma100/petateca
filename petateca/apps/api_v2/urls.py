from django.conf.urls.defaults import *

from piston.authentication import HttpBasicAuthentication
from piston.resource import Resource

from api_v2 import handlers as h

auth = HttpBasicAuthentication(realm="Liberateca v2 API - Autenticacion")
ad = { 'authentication': auth }

serie_resource = Resource(handler=h.SerieHandler, **ad)
season_resource = Resource(handler=h.SeasonHandler, **ad)
episode_resource = Resource(handler=h.EpisodeHandler, **ad)

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'core/api_v2.html'}),
    url(r'^series/$', serie_resource, name='API_v2_serie_list'),
    url(r'^series/(?P<serie_id>\d+)/$', serie_resource, name='API_v2_serie_detail'),

    url(r'^series/(?P<serie_id>\d+)/seasons/$', season_resource, name='API_v2_season_list'),
    url(r'^series/(?P<serie_id>\d+)/(?P<season>\d+)/$', season_resource, name='API_v2_season_detail'),
    url(r'^series/(?P<serie_id>\d+)/(?P<season>\d+)/(?P<episode>\d+)/$', episode_resource, name='API_v2_episode_detail'),
)

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from acquisti.views import get_lista_fornitori, get_lista_prodotti,\
    get_lista_unita_misura, get_ragione_sociale_by_id, get_nome_prodotto_by_id,\
    get_unita_di_misura_by_id

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'invoice2.views.home', name='home'),
    # url(r'^invoice2/', include('invoice2.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'get-lista-fornitori', get_lista_fornitori,),
    url(r'get-lista-prodotti', get_lista_prodotti,),
    url(r'get-lista-unita-misura', get_lista_unita_misura,),

    url(r'get-ragione-sociale-by-id', get_ragione_sociale_by_id,),
    url(r'get-nome-prodotto-by-id', get_nome_prodotto_by_id,),
    url(r'get-unita-di-misura-by-id', get_unita_di_misura_by_id,),
    
)

if not "dolcerende.com" in settings.SITE_URL:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
    )


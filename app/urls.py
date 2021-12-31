from django.urls import path, include

from app import conf

from app.urls_api import api_urlpatterns

urlpatterns = []

urlpatterns += api_urlpatterns

urlpatterns += [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls'))
]

from app.views import movie

urlpatterns += [
    # movie
    path(
        'movie/',
        movie.List.as_view(),
        name=conf.MOVIE_LIST_URL_NAME
    ),
    path(
        'movie/full/',
        movie.ListFull.as_view(),
        name='MOVIE_list_full'
    ),
    path(
        'movie/create/',
        movie.Create.as_view(),
        name=conf.MOVIE_CREATE_URL_NAME
    ),
    path(
        'movie/<int:pk>/',
        movie.Detail.as_view(),
        name=conf.MOVIE_DETAIL_URL_NAME
    ),
    path(
        'movie/<int:pk>/update/',
        movie.Update.as_view(),
        name=conf.MOVIE_UPDATE_URL_NAME
    ),
    path(
        'movie/<int:pk>/delete/',
        movie.Delete.as_view(),
        name=conf.MOVIE_DELETE_URL_NAME
    ),
    path(
        'movie/list/json/',
        movie.MovieListJson.as_view(),
        name=conf.MOVIE_LIST_JSON_URL_NAME
    ),
    path(
        'get-movies',
        movie.get_movies,
        name='get_movies'
    ),
    path(
        'delete-movies',
        movie.delete_all_movies,
        name='delete_all_movies'
    )
]

from app.views import serie

urlpatterns += [
    # serie
    path(
        'serie/',
        serie.List.as_view(),
        name=conf.SERIE_LIST_URL_NAME
    ),
    path(
        'serie/full/',
        serie.ListFull.as_view(),
        name='SERIE_list_full'
    ),
    path(
        'serie/create/',
        serie.Create.as_view(),
        name=conf.SERIE_CREATE_URL_NAME
    ),
    path(
        'serie/<int:pk>/',
        serie.Detail.as_view(),
        name=conf.SERIE_DETAIL_URL_NAME
    ),
    path(
        'serie/<int:pk>/update/',
        serie.Update.as_view(),
        name=conf.SERIE_UPDATE_URL_NAME
    ),
    path(
        'serie/<int:pk>/delete/',
        serie.Delete.as_view(),
        name=conf.SERIE_DELETE_URL_NAME
    ),
    path(
        'serie/list/json/',
        serie.SerieListJson.as_view(),
        name=conf.SERIE_LIST_JSON_URL_NAME
    ),
    path(
        'get-series',
        serie.get_series,
        name='get_series'
    ),
    path(
        'delete-series',
        serie.delete_all_series,
        name='delete_all_series'
    )
]

from app.views import channel

urlpatterns += [
    # channel
    path(
        'channel/',
        channel.List.as_view(),
        name=conf.CHANNEL_LIST_URL_NAME
    ),
    path(
        'channel/full/',
        channel.ListFull.as_view(),
        name='CHANNEL_list_full'
    ),
    path(
        'channel/create/',
        channel.Create.as_view(),
        name=conf.CHANNEL_CREATE_URL_NAME
    ),
    path(
        'channel/<int:pk>/',
        channel.Detail.as_view(),
        name=conf.CHANNEL_DETAIL_URL_NAME
    ),
    path(
        'channel/<int:pk>/update/',
        channel.Update.as_view(),
        name=conf.CHANNEL_UPDATE_URL_NAME
    ),
    path(
        'channel/<int:pk>/delete/',
        channel.Delete.as_view(),
        name=conf.CHANNEL_DELETE_URL_NAME
    ),
    path(
        'channel/list/json/',
        channel.ChannelListJson.as_view(),
        name=conf.CHANNEL_LIST_JSON_URL_NAME
    ),
    path(
        'get-channels',
        channel.get_channels,
        name='get_channels'
    ),
    path(
        'delete-channels',
        channel.delete_all_channels,
        name='delete_all_channels'
    )
]

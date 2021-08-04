from django.urls import include, path
from charts import views

#router.register("amiibo_chart", views.AmiiboChartViewSet)
urlpatterns = [
    #path("", include(router.urls)),
    path('index/', views.index, name='index'),
    path('amiiboSeries/', views.amiiboSeries, name='amiiboSeries'),
    path('gameSeries/', views.gameSeries, name='gameSeries'),
]
from rest_framework.routers import DefaultRouter
from django.urls import include, path
from charts import views

router  = DefaultRouter()

#router.register("amiibo_chart", views.AmiiboChartViewSet)
urlpatterns = [
    path("", include(router.urls)),
]
from django.urls import path

from .views import IndexView, DadosJSONView, RenderChart

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dados/', DadosJSONView.as_view(), name='dados'),
    path('chart1', RenderChart, name='chart1')
]

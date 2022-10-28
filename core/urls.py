from django.urls import path
import core.views

urlpatterns = [
    path('', core.views.IndexView.as_view()),
    path('records/', core.views.allRecords),
    path('records/<int:id>/', core.views.singleRecord),
    path('records/filter', core.views.filterRecords),

    path('charts/', core.views.ChartsView.as_view()),
    path('charts/get_data', core.views.chartDataView),
]
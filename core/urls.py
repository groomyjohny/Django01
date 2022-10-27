from django.urls import path
import core.views

urlpatterns = [
    path('', core.views.index),
    path('records/', core.views.allRecords),
    path('records/<int:id>/', core.views.singleRecord),
    path('records/filter', core.views.filterRecords),

    path('charts/', core.views.chartsView),
]
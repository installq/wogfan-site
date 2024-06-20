from django.urls import path
from wogrecords import views

urlpatterns = [
    path('wog1/', views.index, name = 'index'),
    path('wog1_history/', views.history, name = 'HistoryRecords'),
    path('wog2/', views.index2, name = 'index2'),
    path('wog2_history/', views.history2, name = 'HistoryRecords2'),
    path('leaderboards/',views.leaderboards, name = 'leaderboards'),
]
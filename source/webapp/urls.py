from django.urls import path

from webapp.views import IndexView, CreatePoll, PollView, UpdatePoll, DeletePoll, CreateChoice, UpdateChoice, DeleteChoice, CreateAnswer, DeleteAnswer, UpdateAnswer


urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('polls/add/', CreatePoll.as_view(), name="create_poll"),
    path('poll/<int:pk>/', PollView.as_view(), name="poll_view"),
    path('poll/<int:pk>/update/', UpdatePoll.as_view(), name="update_poll"),
    path('poll/<int:pk>/delete/', DeletePoll.as_view(), name="delete_poll"),
    path('poll/<int:pk>/choice/add/', CreateChoice.as_view(), name="poll_choice_create"),
    path('choices/<int:pk>/update/', UpdateChoice.as_view(), name="update_choice"),
    path('choices/<int:pk>/delete/', DeleteChoice.as_view(), name="delete_choice"),
    path('poll/<int:pk>/answer/add/', CreateAnswer.as_view(), name="create_answer"),
    path('answers/<int:pk>/update/', UpdateAnswer.as_view(), name="update_answer"),
    path('asnwers/<int:pk>/delete/', DeleteAnswer.as_view(), name="delete_answer"),
]
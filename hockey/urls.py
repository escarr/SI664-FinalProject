from django.urls import path, reverse_lazy
from . import views

app_name='hockey'
urlpatterns = [
    path('', views.GamesListView.as_view(), name = 'all'),
    path('game/<int:pk>', views.TicketListView.as_view(), name = 'game_tickets'),
    path('ticket/<int:pk>', views.TicketDetailView.as_view(), name='ticket_detail'),
    path('ticket/create',
        views.TicketCreateView.as_view(success_url=reverse_lazy('hockey:all')), name='ticket_create'),
    path('ticket/<int:pk>/update',
        views.TicketUpdateView.as_view(success_url=reverse_lazy('hockey:all')), name='ticket_update'),
    path('ticket/<int:pk>/delete',
        views.TicketDeleteView.as_view(success_url=reverse_lazy('hockey:all')), name='ticket_delete'),
    path('ticket/<int:pk>/comment',
        views.CommentCreateView.as_view(), name='ticket_comment_create'),
    path('comment/<int:pk>/delete',
        views.CommentDeleteView.as_view(success_url=reverse_lazy('hockeyl')), name='ticket_comment_delete'),

]

# We use reverse_lazy in urls.py to delay looking up the view until all the paths are defined

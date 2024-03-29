from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from football.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from football.forms import CommentForm
from football.models import Ticket, Comment, Game



class TicketListView(OwnerListView):
    model = Ticket
    template_name = "football/ticket_list.html"
    def get(self, request, pk) :
        game = Game.objects.get(id=pk)
        tickets = Ticket.objects.filter(game=game).order_by('section')
        context = { 'game': game, 'ticket_list' : tickets }
        return render(request, self.template_name, context)


class TicketDetailView(OwnerDetailView):
    model = Ticket
    template_name = "football/ticket_detail.html"
    def get(self, request, pk) :
        ticket = Ticket.objects.get(id=pk)
        game = ticket.game
        comments = Comment.objects.filter(ticket=ticket).order_by('-updated_at')
        comment_form = CommentForm()
        context = { 'ticket' : ticket, 'game' : game, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)

class TicketCreateView(OwnerCreateView):
    model = Ticket
    fields = ['sport', 'game', 'section', 'row', 'seat', 'seller', 'price', 'payment_method', 'meetup_spot']
    template_name = "football/ticket_form.html"

class TicketUpdateView(OwnerUpdateView):
    model = Ticket
    fields = ['sport', 'game', 'section', 'row', 'seat', 'price', 'seller', 'payment_method', 'meetup_spot']
    template_name = "football/ticket_form.html"

class TicketDeleteView(OwnerDeleteView):
    model = Ticket
    template_name = "football/ticket_delete.html"

class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        a = get_object_or_404(Ticket, id=pk)
        comment = Comment(text=request.POST['comment'], owner=request.user, ticket=a)
        comment.save()
        return redirect(reverse('football:ticket_detail', args=[pk]))

class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "football/ticket_comment_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        ticket = self.object.ticket
        return reverse('football:ticket_detail', args=[ticket.id])

class GamesListView(OwnerListView):
    model = Game
    template_name = "football/game_list.html"


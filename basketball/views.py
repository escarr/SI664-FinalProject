from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from basketball.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from basketball.forms import CommentForm
from basketball.models import Ticket, Comment, Game


# Create your views here.

class TicketListView(OwnerListView):
    model = Ticket
    template_name = "basketball/ticket_list.html"
    def get(self, request, pk) :
        game = Game.objects.get(id=pk)
        tickets = Ticket.objects.filter(game=game)
        context = { 'game': game, 'ticket_list' : tickets }
        return render(request, self.template_name, context)

class TicketDetailView(OwnerDetailView):
    model = Ticket
    template_name = "basketball/ticket_detail.html"
    def get(self, request, pk) :
        ticket = Ticket.objects.get(id=pk)
        game = ticket.game
        comments = Comment.objects.filter(ticket=ticket).order_by('-updated_at')
        comment_form = CommentForm()
        context = { 'ticket' : ticket, 'game' : game, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)

class TicketCreateView(OwnerCreateView):
    model = Ticket
    fields = ['sport', 'game', 'seller', 'price', 'payment_method', 'meetup_spot']
    template_name = "basketball/ticket_form.html"

class TicketUpdateView(OwnerUpdateView):
    model = Ticket
    fields = ['sport', 'game', 'price', 'seller', 'payment_method', 'meetup_spot']
    template_name = "basketball/ticket_form.html"

class TicketDeleteView(OwnerDeleteView):
    model = Ticket
    template_name = "basketball/ticket_delete.html"

class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        a = get_object_or_404(Ticket, id=pk)
        comment = Comment(text=request.POST['comment'], owner=request.user, ticket=a)
        comment.save()
        return redirect(reverse('basketball:ticket_detail', args=[pk]))

class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "basketball/ticket_comment_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        ticket = self.object.ticket
        return reverse('basketball:ticket_detail', args=[ticket.id])


class GamesListView(OwnerListView):
    model = Game
    template_name = "basketball/game_list.html"

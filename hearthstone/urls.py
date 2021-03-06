from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='app_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='app_logout'),
    path('party/', views.party, name='game'),
    path('sell-card/<int:herouser_id>', views.sellCard, name='sellCard'),
    path('buy-cards/', views.buyCards, name='buyCards'),
    path('my-cards/', views.myCards, name='myCards'),
    path('my-decks/', views.myDecks, name='myDecks'),
    path('deck/<int:deck_id>', views.deck, name='deck'),
    path('deck/delete/<int:deck_id>', views.deleteDeck, name='deckDelete'),
    path('deck/update/<int:deck_id>', views.updateDeck, name='deckUpdate'),
    path('deck/create', views.createDeck, name='deckCreate'),
    path('deck/create/<int:hero_id>', views.createDeckByHero, name='createDeckByHero'),
]
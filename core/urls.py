from django.urls import path
from .views import HomeView, MoreView,PantsView, PolosView, HatsView,AboutView, ContactView, RulesView, PrivacyView, CookieView, DeliveriesView ,OrdersView, Tee1View, Tee2View, Tee3View, Tee4View, Tee5View, Hats1View, Hats2View


app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name= 'home'),
    path('more', MoreView.as_view(), name= 'more'),
    path('tehilians_hats', HatsView.as_view(), name= 'tehilians_hats'),
    path('tehilians_polos', PolosView.as_view(), name= 'tehilians_polos'),
    path('tehilians_pants', PantsView.as_view(), name= 'tehilians_pants'),
    path('about', AboutView.as_view(), name= 'about'),
    path('contact_us', ContactView.as_view(), name= 'contact_us'),
    path('rules', RulesView.as_view(), name= 'rules'),
    path('privacy_policy', PrivacyView.as_view(), name= 'privacy_policy'),
    path('cookie_notice', CookieView.as_view(), name= 'cookie_notice'),
    path('howtoorder', OrdersView.as_view(), name='howtoorder'),
    path('ouroptions', DeliveriesView.as_view(), name= 'ouroptions'),
    path('whiteplaintee', Tee1View.as_view(), name= 'whiteplaintee'),
    path('graphicswhitetee', Tee2View.as_view(), name= 'graphicswhitetee'),
    path('theboystee', Tee3View.as_view(), name= 'theboystee'),
    path('plaintee',Tee4View.as_view(), name= 'plaintee'),
    path('femalewhitetee', Tee5View.as_view(), name= 'femalewhitetee'),
    path('hats1', Hats1View.as_view(), name= 'hats1'),
    path('hats2', Hats2View.as_view(), name= 'hats2'),
]
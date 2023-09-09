#from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class MoreView(TemplateView):
    template_name = 'more.html'
    
class PantsView(TemplateView):
    template_name = 'tehilians_pants.html'

class PolosView(TemplateView):
    template_name = 'tehilians_polos.html'

class HatsView(TemplateView):
    template_name = 'tehilians_hats.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact_us.html'

class RulesView(TemplateView):
    template_name= 'rules.html'

class PrivacyView(TemplateView):
    template_name= 'privacy_policy.html'

class CookieView(TemplateView):
    template_name= 'cookie_notice.html'

class OrdersView(TemplateView):
    template_name= 'howtoorder.html'

class DeliveriesView(TemplateView):
    template_name= 'ouroptions.html'

class Tee1View(TemplateView):
    template_name= 'whiteplaintee.html'

class Tee2View(TemplateView):
    template_name= 'graphicswhitetee.html'

class Tee3View(TemplateView):
    template_name= 'theboystee.html'

class Tee4View(TemplateView):
    template_name= 'plaintee.html'

class Tee5View(TemplateView):
    template_name= 'femalewhitetee.html'

class Hats1View(TemplateView):
    template_name= 'hats1.html'

class Hats2View(TemplateView):
    template_name= 'hats2.html'
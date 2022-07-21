from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = 'jumpei'
        return ctxt

    
class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = 'jumpei'
        ctxt["num_services"] = 123456789
        ctxt["skills"] = [
            "shopppingApp",
            "lineApp",
            "googlemapApp",        
        ]
        return ctxt
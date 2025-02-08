from django.views.generic import TemplateView


class IndexView(TemplateView):
    """Gets the index page."""

    template_name: str = "core/index.html"

from django.http import HttpResponseBase
from django.test import TestCase
from django.urls import reverse


class TestIndexView(TestCase):
    """Test the index view."""

    url: str = reverse("core:index")

    def test_index_view_status_code(self) -> None:
        """Test that the index view returns a 200 status code."""
        response: HttpResponseBase = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_index_view_template_used(self) -> None:
        """Test that the correct template is used for the index view."""
        response: HttpResponseBase = self.client.get(self.url)
        self.assertTemplateUsed(response, "core/index.html")

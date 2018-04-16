from django.test import TestCase
class TestViews(TestCase):
    def test_welcome_view(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code,200)
    def test_download_view(self):
        response = self.client.get("/download/1")
        self.assertEqual(response.get("Content-Disposition"),
                         "inline; filename=1.png")


from django.db import models

# Create your models here.


from django.db import models


class Request(models.Model):
    url = models.URLField()
    method = models.CharField(max_length=10)
    headers = models.JSONField()
    body = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.method} {self.url}"


class Response(models.Model):
    request = models.OneToOneField(
        Request, on_delete=models.CASCADE, related_name="response"
    )
    status_code = models.IntegerField()
    headers = models.JSONField()
    body = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response to {self.request.url} - {self.status_code}"

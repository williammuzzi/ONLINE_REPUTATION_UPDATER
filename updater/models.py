from django.db import models

class POI(models.Model):
    poiid = models.CharField(max_length=50, primary_key=True)
    dealerid = models.CharField(max_length=50)
    email_poc = models.EmailField()
    ordered_timestamp = models.DateTimeField(null=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.poiid} - {self.email_poc}"

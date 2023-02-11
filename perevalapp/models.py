from django.db import models

class pereval_added (models.Model):
    PEN = "PENGING"
    ACC = "ACCEPTED"
    REJ = "REJECTED"
    STATUS_CHOICES = [
        (PEN, 'pending'),
        (ACC, 'accepted'),
        (REJ, 'rejected')
    ]
    date_added = models.DateTimeField(auto_now_add=True)
    row_data = models.JSONField()
    images = models.JSONField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')


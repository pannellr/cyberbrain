import datetime
from django.db import models


class Leaf(models.Model):
	    mac_address = models.CharField(max_length=200)
	    last_seen_date = models.DateTimeField(auto_now=True)

from django.contrib import admin
from .models import Vote, VoteCount

admin.site.register(Vote)
admin.site.register(VoteCount)

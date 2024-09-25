from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Vote, VoteCount

@receiver(post_save, sender=Vote)
def update_vote_count_on_save(sender, instance, **kwargs):
    vote_count, created = VoteCount.objects.get_or_create(name=instance.participate_name)

    vote_count.total_vote = Vote.objects.filter(participate_name=instance.participate_name).count()
    vote_count.save()
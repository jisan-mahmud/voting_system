from django.db import models


class Vote(models.Model):
    voter_name = models.CharField(max_length= 100)
    participate_name = models.CharField(max_length= 100)
    voter_count = models.IntegerField(default= 0, blank= True, null= True)

    def __str__(self) -> str:
        return self.voter_name
    
class VoteCount(models.Model):
    name = models.CharField(max_length= 100)
    total_vote = models.IntegerField(default= 1, blank= True, null= True)

    def __str__(self) -> str:
        return f'{self.name} {self.total_vote}'
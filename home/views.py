from django.shortcuts import render
from .forms import VoteForm
from .models import Vote, VoteCount
def home(request):
    if request.method == 'POST':
        form = VoteForm(data= request.POST)
        if form.is_valid():
            voter_name = form.cleaned_data.get('voter_name')
            has_voter = Vote.objects.filter(voter_name__icontains = voter_name)
            if has_voter.exists():
                vote = Vote.objects.get(voter_name__icontains = voter_name)
                if vote.voter_count < 2:
                    vote.participate_name = form.cleaned_data['participate_name']
                    vote.voter_count = vote.voter_count + 1
                    vote.save()

                    # total vote count 
                    vote_count, created = VoteCount.objects.get_or_create(name=form.cleaned_data['participate_name'])
                    vote_count.total_vote = Vote.objects.filter(participate_name=form.cleaned_data['participate_name']).count()
                    vote_count.save()
                else:
                    print('Limit exits.')

            else:
                print('No')
                vote = form.save()
                vote.voter_count = vote.voter_count + 1
                vote.save()

                 # total vote count 
                vote_count, created = VoteCount.objects.get_or_create(name=form.cleaned_data['participate_name'])
                vote_count.total_vote = Vote.objects.filter(participate_name=form.cleaned_data['participate_name']).count()
                vote_count.save()
    return render(request, 'home/index.html')
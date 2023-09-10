from django.db.models import Avg, Func
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddScorecard
from .models import Player, YahtzeeScorecard


# Create your views here.
def home(request):
    players = Player.objects.all()

    # Check if logging in
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')
        else:
            messages.success(request, "There was an error, please try again.")
            return redirect('home')

    return render(request, 'home.html', {'players': players})


# def login_user(request):
#     pass


def logout_user(request):
    logout(request)
    messages.success(request, "Logout Successful")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            Player.objects.create(username=user.username, first_name=user.first_name, last_name=user.last_name,
                                  email=user.email)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})


def player_info(request, pk):
    # If user is logged in
    if request.user.is_authenticated:
        # Look up player
        player_info = Player.objects.get(id=pk)
        return render(request, 'player.html', {'player_info': player_info})

    else:
        messages.success(request, "Please login to view this page")
        return redirect('home')


def add_scorecard(request):
    form = AddScorecard(request.POST or None)
    if request.user.is_authenticated:

        if request.method == "POST":
            if not form.is_valid():
                print("fuck")
                return render(request, 'add_scorecard.html', {'form': form})

            if form.is_valid():
                username = form.cleaned_data['username']

                ones = form.cleaned_data['ones']
                twos = form.cleaned_data['twos']
                threes = form.cleaned_data['threes']
                fours = form.cleaned_data['fours']
                fives = form.cleaned_data['fives']
                sixes = form.cleaned_data['sixes']
                three_of_a_kind = form.cleaned_data['three_of_a_kind']
                four_of_a_kind = form.cleaned_data['four_of_a_kind']
                full_house = form.cleaned_data['full_house']
                small_straight = form.cleaned_data['small_straight']
                large_straight = form.cleaned_data['large_straight']
                yahtzee = form.cleaned_data['yahtzee']
                yahtzee_bonus = form.cleaned_data['yahtzee_bonus']
                chance = form.cleaned_data['chance']

                upper_total = ones + twos + threes + fours + fives + sixes

                if upper_total >= 63:
                    upper_bonus = 35

                else:
                    upper_bonus = 0

                upper_total += upper_bonus

                lower_total = three_of_a_kind + four_of_a_kind + full_house + small_straight + large_straight + yahtzee + yahtzee_bonus + chance

                grand_total = upper_total + lower_total

                scorecard = YahtzeeScorecard(
                    username=username,
                    ones=ones,
                    twos=twos,
                    threes=threes,
                    fours=fours,
                    fives=fives,
                    sixes=sixes,
                    upper_total=upper_total,
                    upper_bonus=upper_bonus,
                    three_of_a_kind=three_of_a_kind,
                    four_of_a_kind=four_of_a_kind,
                    full_house=full_house,
                    small_straight=small_straight,
                    large_straight=large_straight,
                    yahtzee=yahtzee,
                    yahtzee_bonus=yahtzee_bonus,
                    chance=chance,
                    lower_total=lower_total,
                    grand_total=grand_total,
                )
                scorecard.save()
                form = AddScorecard()

                messages.success(request, "Scorecard added!")

        return render(request, 'add_scorecard.html', {'form': form})

    else:
        messages.success(request, "Please login to view this page")
        return redirect('home')


def view_scorecard(request):
    # scorecard_info = YahtzeeScorecard.objects.values('username__username').annotate(average_grand_total=Func(Avg('grand_total'), function='CEIL')).order_by('-average_grand_total')
    return render(request, 'view_scorecard.html')


def top_10_scorecards(request):
    scorecard_info = YahtzeeScorecard.objects.order_by('-grand_total')[:10]
    player = Player.objects.all()
    return render(request, 'top_10_scorecards.html', {'scorecard_info': scorecard_info})


def top_10_lowest(request):
    scorecard_info = YahtzeeScorecard.objects.order_by('grand_total')[:10]
    player = Player.objects.all()
    return render(request, 'top_10_lowest.html', {'scorecard_info': scorecard_info})


def avg_grand_total(request):
    scorecard_info = YahtzeeScorecard.objects.values('username__username').annotate(average_grand_total=Func(Avg('grand_total'), function='CEIL')).order_by('-average_grand_total')
    return render(request, 'avg_grand_total.html', {'scorecard_info': scorecard_info})


def all_scorecards(request):
    scorecard_info = YahtzeeScorecard.objects.all().order_by('-scorecard_id')
    player = Player.objects.all()
    return render(request, 'all_scorecards.html', {'scorecard_info': scorecard_info})


def detail_scorecard(request, pk):
    # If user is logged in
    if request.user.is_authenticated:
        # Look up player
        detail_scorecard = YahtzeeScorecard.objects.get(scorecard_id=pk)
        return render(request, 'detail_scorecard.html', {'detail_scorecard': detail_scorecard})

    else:
        messages.success(request, "Please login to view this page")
        return redirect('home')


def delete_scorecard(request, pk):
    if request.user.is_authenticated:
        delete_it = YahtzeeScorecard.objects.get(scorecard_id=pk)
        delete_it.delete()
        messages.success(request, "Scorecard Deleted Successfully")
        return redirect('view_scorecard')
    else:
        messages.success(request, "You Must Be Logged In To Do That...")
        return redirect('view_scorecard')


def update_scorecard(request, pk):
    if request.user.is_authenticated:
        current_scorecard = YahtzeeScorecard.objects.get(scorecard_id=pk)
        form = AddScorecard(request.POST or None, instance=current_scorecard)

        if form.is_valid():
            form.save()
            messages.success(request, "Scorecard Updated Successfully")
            return redirect('view_scorecard')
        return render(request, 'update_scorecard.html', {'form': form})
    else:
        messages.success(request, "You Must Be Logged In To Do That...")
        return redirect('view_scorecard')

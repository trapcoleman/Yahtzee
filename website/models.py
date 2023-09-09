from django.db import models


class Player(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class YahtzeeScorecard(models.Model):
    username = models.ForeignKey(Player, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    scorecard_id = models.AutoField(primary_key=True)
    ones = models.IntegerField(default=0)
    twos = models.IntegerField(default=0)
    threes = models.IntegerField(default=0)
    fours = models.IntegerField(default=0)
    fives = models.IntegerField(default=0)
    sixes = models.IntegerField(default=0)
    upper_total = models.IntegerField(default=0)
    upper_bonus = models.IntegerField(default=0)
    three_of_a_kind = models.IntegerField(default=0)
    four_of_a_kind = models.IntegerField(default=0)
    full_house = models.IntegerField(default=0)
    small_straight = models.IntegerField(default=0)
    large_straight = models.IntegerField(default=0)
    yahtzee = models.IntegerField(default=0)
    chance = models.IntegerField(default=0)
    yahtzee_bonus = models.IntegerField(default=0)
    lower_total = models.IntegerField(default=0)
    grand_total = models.IntegerField(default=0)

    def __str__(self):
        del self.field['upper_total']
        return f"Scorecard {self.scorecard_id} for {self.username.first_name, self.username.last_name}"


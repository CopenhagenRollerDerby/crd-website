from django.db import models

class Address(models.Model):
    name = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    additional_line = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.IntegerField()
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)

    location = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    url = models.URLField(null=True, blank=True)

    description = models.TextField()

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

class MatchDay(Event):
    image = models.ImageField(upload_to = 'matches/')


class Match(models.Model):
    start_time = models.DateTimeField(null=True, blank=True)

    match_day = models.ForeignKey(MatchDay, on_delete=models.CASCADE)
    home_team = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name='match_home')
    away_team = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name='match_away')

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"

from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    class Meta:
        db_table = 'teams'
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100)
    class Meta:
        db_table = 'users'
    def __str__(self):
        return self.email

class Activity(models.Model):
    user = models.EmailField()
    type = models.CharField(max_length=50)
    distance = models.FloatField()
    class Meta:
        db_table = 'activities'
    def __str__(self):
        return f"{self.user} - {self.type}"

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        db_table = 'leaderboard'
    def __str__(self):
        return f"{self.team}: {self.points}"

class Workout(models.Model):
    user = models.EmailField()
    workout = models.CharField(max_length=100)
    reps = models.IntegerField()
    class Meta:
        db_table = 'workouts'
    def __str__(self):
        return f"{self.user} - {self.workout}"
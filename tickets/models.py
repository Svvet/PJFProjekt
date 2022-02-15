from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Play(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Hall(models.Model):
    name = models.CharField(max_length=100)
    seats = models.IntegerField();

    def __str__(self):
        return self.name + ' ' + str(self.seats)


class Performance(models.Model):
    play = models.ForeignKey(Play, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, default=1)
    perf_date = models.DateTimeField("Performance date")

    def __str__(self):
        return "Id: " + str(self.pk) + "; Sztuka: " + self.play.title + "; Sala: " + self.hall.name


class Ticket(models.Model):
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE)
    seat = models.IntegerField()
    row = models.IntegerField(default=None)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

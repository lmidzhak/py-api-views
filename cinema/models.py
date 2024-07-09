from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "genres"


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = "actors"


class CinemaHall(models.Model):
    name = models.CharField(max_length=255, unique=True)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self):
        return (
            f"Cinema hall {self.name}: {self.rows} rows "
            f"with {self.seats_in_row} in a row"
        )

    class Meta:
        verbose_name_plural = "cinema_halls"


class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    actors = models.ManyToManyField(
        Actor,
        blank=True,
        related_name="movies"
    )
    genres = models.ManyToManyField(
        Genre,
        blank=True,
        related_name="movies"
    )
    duration = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "movies"

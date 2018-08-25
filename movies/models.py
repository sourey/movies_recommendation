from django.db import models
class Movies(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    budget = models.BigIntegerField(blank=True, null=True)
    genres = models.TextField(blank=True, null=True)
    homepage = models.TextField(blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)
    keywords = models.TextField(blank=True, null=True)
    original_language = models.TextField(blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    popularity = models.FloatField(blank=True, null=True)
    revenue = models.BigIntegerField(blank=True, null=True)
    runtime = models.BigIntegerField(blank=True, null=True)
    tagline = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    vote_average = models.FloatField(blank=True, null=True)
    vote_count = models.BigIntegerField(blank=True, null=True)
    movie_id = models.BigIntegerField(blank=True, null=True)
    cast = models.TextField(blank=True, null=True)
    director = models.TextField(blank=True, null=True)
    year = models.BigIntegerField(blank=True, null=True)
    imdb_id = models.TextField(blank=True, null=True)
    poster_path = models.TextField(blank=True, null=True)
    num_critic_for_reviews = models.BigIntegerField(blank=True, null=True)
    num_user_for_reviews = models.BigIntegerField(blank=True, null=True)
    imdb_score = models.FloatField(blank=True, null=True)
    movie_facebook_likes = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'movies'
        verbose_name_plural="Movies"
    def __str__(self):
    	return self.title



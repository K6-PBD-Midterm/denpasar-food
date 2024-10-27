from django.db import models
from django.contrib.auth.models import User
from restaurants.models import Restaurant  

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant_reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.restaurant.name} Review by {self.user.username}'

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        unique_together = ('user', 'restaurant')

    def __str__(self):
        return f'{self.user.username} likes {self.restaurant.name}'
    
class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='dislikes')

    class Meta:
        unique_together = ('user', 'restaurant')

    def __str__(self):
        return f'{self.user.username} dislikes {self.restaurant.name}'

import csv
import json
from django.core.management.base import BaseCommand
from restaurants.models import Restaurant

class Command(BaseCommand):
    help = 'Load restaurants from a CSV file'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Restaurant.objects.all().delete()

        with open('restaurants-in-denpasar.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                detailed_address = json.loads(row['detailed_address']) if row['detailed_address'] else {}
                reviews_per_rating = json.loads(row['reviews_per_rating']) if row['reviews_per_rating'] else {}
                review_keywords = json.loads(row['review_keywords']) if row['review_keywords'] else {}
                open_hours = json.loads(row['open_hours']) if row['open_hours'] else {}
                cuisines = json.loads(row['cuisines']) if row['cuisines'] else {}
                diets = json.loads(row['diets']) if row['diets'] else {}
                meal_types = json.loads(row['meal_types']) if row['meal_types'] else {}
                dining_options = json.loads(row['dining_options']) if row['dining_options'] else {}
                owner_types = json.loads(row['owner_types']) if row['owner_types'] else {}
                top_tags = json.loads(row['top_tags']) if row['top_tags'] else {}
                ranking = json.loads(row['ranking']) if row['ranking'] else {}

                Restaurant.objects.create(
                    id=row['id'],
                    name=row['name'][:255],  # Truncate the name to 255 characters
                    description=row['description'][:255],  # Truncate the description to 255 characters
                    rating=row['rating'],
                    link=row['link'][:200],  # Truncate the link to 200 characters
                    email=row['email'][:254],
                    phone=row['phone'][:50],  # Truncate the phone to 50 characters
                    website=row['website'][:200],  # Truncate the website to 200 characters
                    image_url=row['featured_image'][:200],  # Truncate the image_url to 200 characters
                    ranking=ranking,
                    address=row['address'][:255],  # Truncate the address to 255 characters
                    detailed_address=detailed_address,
                    latitude=row['latitude'],
                    longitude=row['longitude'],
                    reviews_per_rating=reviews_per_rating,
                    review_keywords=review_keywords,
                    is_open=row['is_open'],
                    open_hours=open_hours,
                    menu_link=row['menu_link'][:200],  # Truncate the menu_link to 200 characters
                    delivery_url=row['delivery_url'][:200],  # Truncate the delivery_url to 200 characters
                    price_range=row['price_range'][:50],  # Truncate the price_range to 50 characters
                    cuisines=cuisines,
                    diets=diets,
                    meal_types=meal_types,
                    dining_options=dining_options,
                    owner_types=owner_types,
                    top_tags=top_tags,
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded restaurants'))
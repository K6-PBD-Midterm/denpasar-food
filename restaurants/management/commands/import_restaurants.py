import json
from django.core.management.base import BaseCommand
from restaurants.models import Restaurant
from django.conf import settings
from pathlib import Path

class Command(BaseCommand):
    help = 'Import restaurants from JSON file'

    def handle(self, *args, **options):
        json_file_path = Path(settings.BASE_DIR) / 'export.json'
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Define a list of amenities to import (both "restaurant" and "fast_food")
        allowed_amenities = ['restaurant', 'fast_food']

        for element in data['elements']:
            if element['type'] == 'node' and 'tags' in element and element['tags'].get('amenity') in allowed_amenities:
                # Check if the restaurant already exists
                osm_id = element['id']
                restaurant, created = Restaurant.objects.update_or_create(
                    osm_id=osm_id,
                    defaults={
                        'name': element['tags'].get('name', ''),
                        'latitude': element['lat'],
                        'longitude': element['lon'],
                        'amenity': element['tags'].get('amenity', ''),
                        'cuisine': element['tags'].get('cuisine', ''),
                        'street': element['tags'].get('addr:street', ''),
                        'postcode': element['tags'].get('addr:postcode', ''),
                        'email': element['tags'].get('email', ''),
                        'phone': element['tags'].get('phone', ''),
                        'website': element['tags'].get('website', ''),
                        'city': element['tags'].get('addr:city', ''),
                        'housenumber': element['tags'].get('addr:housenumber', ''),
                    }
                )
                
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created restaurant: {osm_id}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Updated restaurant: {osm_id}'))

        self.stdout.write(self.style.SUCCESS('Successfully imported/restaurants updated.'))


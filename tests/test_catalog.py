"""
Aether.ist Katalog ve URL Doğrulama Testleri
"""

import os
import sys
import unittest
import json

# Scripts klasörünü path'e ekle
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts"))

from tmdb_client import (
    slugify,
    build_aether_movie_url,
    build_aether_tv_url,
    resolve_categories,
    resolve_platform,
    format_turkish_date,
    tmdb_request
)

class TestAetherCatalog(unittest.TestCase):

    def test_slugify(self):
        self.assertEqual(slugify("The Walking Dead: Dead City"), "the-walking-dead-dead-city")
        self.assertEqual(slugify("Squid Game"), "squid-game")

    def test_aether_urls(self):
        movie_url = build_aether_movie_url(550, "Fight Club")
        self.assertEqual(movie_url, "https://aether.ist/media/tmdb-movie-550-fight-club")
        
        tv_url = build_aether_tv_url(194583, "The Walking Dead: Dead City")
        self.assertEqual(tv_url, "https://aether.ist/media/tmdb-tv-194583-the-walking-dead-dead-city")

    def test_turkish_priority_category(self):
        tr_item = {
            "original_language": "tr",
            "genre_ids": [18, 80]
        }
        categories_str, genres_list = resolve_categories(tr_item, "tv")
        self.assertIn("Türk Yapımı", genres_list)
        self.assertIn("Dram", genres_list)
        self.assertIn("Suç", genres_list)

    def test_tmdb_connection(self):
        data = tmdb_request("/movie/550")
        self.assertIsNotNone(data)
        self.assertEqual(data.get("id"), 550)

if __name__ == "__main__":
    unittest.main()

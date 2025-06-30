import unittest
from cgi import print_environ_usage
from unittest.mock import patch
from dao.VirtualArtGalleryImpl import VirtualArtGalleryImpl
from entities.artist import Artist
from entities.artwork import Artwork
from entities.gallery import Gallery
from entities.users import User
from entities.artwork_gallery import ArtworkGallery
from entities.user_favorite_artwork import UserFavoriteArtwork
from exception.exceptions import ArtistNotFoundException, ArtworkNotFoundException, GalleryNotFoundException, UserNotFoundException, MappingNotFoundException


class TestVirtualArtGallery(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.service = VirtualArtGalleryImpl()

    def test_add_artwork(self):
        art = Artwork(
            artwork_id=None,
            title = "Test Art Uploaded",
            description="Uploaded for test",
            creation_date = "2022-05-10",
            medium="Oil on canvas",
            image_url="Test_art.jpg",
            artist_id= 101
        )
        result = self.service.add_artwork(art)
        self.assertTrue(result)

    def test_update_artwork(self):
        temp_art = Artwork(
            artwork_id=None,
            title="Temp art for update",
            description="To be updated",
            creation_date="2023-01-01",
            medium="Oil on canvas",
            image_url="temp.jpg",
            artist_id= 102
        )
        self.service.add_artwork(temp_art)
        results = self.service.search_artworks("Temp Art for Update")
        if not results:
            self.fail("temp artwork not added")
        artwork_id = results[0][0]
        with patch('builtins.input', side_effect =[
            "Updated Title",
            "",
            "",
            "Oil",
            "",
            102
        ]):
            result = self.service.update_artwork(artwork_id)
            self.assertTrue(result)


    def test_remove_artwork(self):
        temp_art = Artwork(
            artwork_id=None,
            title= "temp art",
            description="to be deleted",
            creation_date="2021-06-06",
            medium="sketch",
            image_url="temp.jpg",
            artist_id=101
        )
        self.service.add_artwork(temp_art)
        results = self.service.search_artworks("temp art")
        if results:
            last_id = results[-1][0]
            results = self.service.remove_artwork(last_id)
            self.assertTrue(results)
        else:
            self.fail("temp not added ")

    def test_search_artworks(self):
        result = self.service.search_artworks("Fall among silence")
        self.assertTrue(result)

    def test_add_gallery(self):
        gallery = Gallery(
            gallery_id = None,
            gallery_name="Thomas PLC",
            gallery_description="Showcases vibrant watercolour and digital pieces from global creators",
            gallery_location="TiffanyTown",
            curator_id=102,
            opening_hours="9AM onwards"
        )
        result = self.service.add_gallery(gallery)
        self.assertTrue(result)
        self.assertIsNotNone(gallery.gallery_id)

    def test_update_gallery(self):
        temp_gallery = Gallery(
            gallery_name="Morgan Ltd",
            gallery_description="A contemporary space highlighting nostalgic and memory-based artworks.",
            gallery_location="West Issac",
            curator_id=102,
            opening_hours="9AM Onwards"
        )
        self.service.add_gallery(temp_gallery)
        results = self.service.search_gallery("Morgan Ltd")
        if not results:
            self.fail("Gallery not added")
        gallery_id = results[0][0]

        with patch('builtins.input', side_effect=[
            "",
            "",
            "West port dylan",
            "",
            ""
        ]):
            result = self.service.update_gallery(gallery_id)
            self.assertTrue(result)

    def test_remove_gallery(self):
        temp_gallery = Gallery(
            gallery_name="Williams-Riverea",
            gallery_description="Known for layered acrylics and modern emotional expressions.",
            gallery_location="Lake Jennifer",
            curator_id=101,
            opening_hours="9AM onwards"
        )
        self.service.add_gallery(temp_gallery)
        results = self.service.search_gallery(temp_gallery.gallery_name)
        gallery_id = results[0][0]
        removal_result = self.service.remove_gallery(gallery_id)
        self.assertTrue(removal_result)

    def test_search_gallery(self):
        result = self.service.search_gallery("Smith Inc")
        self.assertTrue(result)

    def test_add_artwork_to_favorite(self):
        success = self.service.add_artwork_to_favourite(403,212)
        self.assertTrue(success)
        print("Artwork added to favorites")

    def test_get_user_favorite_artworks(self):
        favorites = self.service.get_user_favourite_artworks(401)
        self.assertIsInstance(favorites, list)
        print("Favorites", [art[1] for art in favorites])

    def test_remove_artwork_from_favorites(self):
        success = self.service.remove_artwork_from_favourite(403, 212)
        self.assertTrue(success)

    def test_update_favorite_artwork(self):
        result = self.service.update_favorites_artwork(402, 209,212)
        self.assertTrue(result)

    def test_add_artwork_to_gallery(self):
        success = self.service.add_artwork_to_gallery(211, 313)
        self.assertTrue(success)

    def test_get_artworks_by_gallery(self):
        artworks = self.service.get_artworks_by_gallery(302)
        self.assertIsInstance(artworks, list)
        print("Artworks in gallery", [art[1] for art in artworks])


    def test_remove_artwork_from_galleru(self):
        success = self.service.remove_artwork_from_gallery(211, 313)
        self.assertTrue(success)


if __name__ == "__main__":
    unittest.main()
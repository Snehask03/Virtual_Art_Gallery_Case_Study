from abc import ABC, abstractmethod

class IVirtualArtGallery(ABC):

    #Artist Management:
    @abstractmethod
    def add_artist(self, artist):
        pass

    @abstractmethod
    def update_artist(self, artist_id):
        pass

    @abstractmethod
    def remove_artist(self, artist_id):
        pass

    @abstractmethod
    def get_artist_by_id(self, artist_id):
        pass

    @abstractmethod
    def search_artists(self, keyword):
        pass

    @abstractmethod
    def deactivate_artist(self, artist_id):
        pass

    # Artwork Management
    @abstractmethod
    def add_artwork(self, artwork):
        pass

    @abstractmethod
    def update_artwork(self, artwork):
        pass

    @abstractmethod
    def remove_artwork(self, artwork_id):
        pass

    @abstractmethod
    def get_artwork_by_id(self, artwork_id):
        pass

    @abstractmethod
    def search_artworks(self, keyword):
        pass

    # Gallery Management
    @abstractmethod
    def add_gallery(self, gallery):
        pass

    @abstractmethod
    def update_gallery(self, gallery_id):
        pass

    @abstractmethod
    def remove_gallery(self, gallery_id):
        pass

    @abstractmethod
    def find_gallery(self, gallery_id):
        pass

    @abstractmethod
    def search_galleries(self, keyword):
        pass

    @abstractmethod
    def deactivate_gallery(self, gallery_id):
        pass

    #User management
    @abstractmethod
    def add_user(self, user):
        pass

    @abstractmethod
    def find_user(self, user_id):
        pass

    @abstractmethod
    def update_user(self, user_id):
        pass

    @abstractmethod
    def remove_user(self, user_id):
        pass

    @abstractmethod
    def search_user(self, keyword):
        pass

    @abstractmethod
    def deactivate_user(self, user_id):
        pass

    #Artwork-Gallery Junction table:
    @abstractmethod
    def add_artwork_to_gallery(self, artwork_id, gallery_id):
        pass

    @abstractmethod
    def get_artwork_by_gallery(self, gallery_id):
        pass

    @abstractmethod
    def get_galleries_by_artwork(self, artwork_id):
        pass

    @abstractmethod
    def remove_artwork_from_gallery(self, artwork_id, gallery_id):
        pass


    #User Favourites
    @abstractmethod
    def add_artwork_to_favourite(self, user_id, artwork_id):
        pass

    @abstractmethod
    def remove_artwork_from_favourite(self, user_id, artwork_id):
        pass

    @abstractmethod
    def get_user_favourite_artworks(self, user_id):
        pass


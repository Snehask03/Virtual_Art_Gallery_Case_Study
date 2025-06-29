class ArtworkGallery:
    def __init__(self, artwork_id = None, gallery_id = None):
        self.__artwork_id = artwork_id
        self.__gallery_id = gallery_id

    def __str__(self):
        return (
            f"ArtworkGallery [Artwork ID = {self.artwork_id}, Gallery ID = {self.gallery_id}]"
        )

    # Getters and Setters
    @property
    def artwork_id(self):
        return self.__artwork_id
    @artwork_id.setter
    def artwork_id(self, artwork_id):
        self.__artwork_id = artwork_id

    @property
    def gallery_id(self):
        return self.__gallery_id
    @gallery_id.setter
    def gallery_id(self, gallery_id):
        self.__gallery_id = gallery_id

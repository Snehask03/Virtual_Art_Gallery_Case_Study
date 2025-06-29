class Artwork:
    def __init__(self, artwork_id = None, title = None, description = None, creation_date = None, medium = None, image_url = None, artist_id = None):
        self.__artwork_id = artwork_id
        self.__title = title
        self.__description = description
        self.__creation_date =  creation_date
        self.__medium = medium
        self.__image_url = image_url
        self.__artist_id = artist_id # foreign key

    def __str__(self):
        return (
            f"Artwork [ID = {self.artwork_id}, Title = '{self.title}',\n"
            f"Description = '{self.description}', Creation Date = {self.creation_date},\n"
            f"Medium = '{self.medium}', Image URL = '{self.image_url}',\n"
            f"Artist ID = {self.artist_id}]"
        )

    # Getters and Setters
    @property
    def artwork_id(self):
        return self.__artwork_id
    @artwork_id.setter
    def artwork_id(self, artwork_id):
        self.__artwork_id = artwork_id

    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def creation_date(self):
        return self.__creation_date
    @creation_date.setter
    def creation_date(self, creation_date):
        self.__creation_date = creation_date

    @property
    def medium(self):
        return self.__medium
    @medium.setter
    def medium(self, medium):
        self.__medium = medium

    @property
    def image_url(self):
        return self.__image_url
    @image_url.setter
    def image_url(self, image_url):
        self.__image_url = image_url

    @property
    def artist_id(self):
        return self.__artist_id

    @artist_id.setter
    def artist_id(self, artist_id):
        self.__artist_id = artist_id






    # def get_artwork_id(self):
    #     return self.__ArtworkID
    #
    # def get_title(self):
    #     return self.__Title
    #
    # def get_description(self):
    #     return self.__Description
    #
    # def get_creation_date(self):
    #     return self.__CreationDate
    #
    # def get_medium(self):
    #     return self.__Medium
    #
    # def get_image_url(self):
    #     return self.__ImageURL
    #
    # def get_artist_id(self):
    #     return self.__ArtistID
    #
    # #Setters
    # def set_artwork_id(self, ArtworkID):
    #     self.__ArtworkID = ArtworkID
    #
    # def set_title(self, Title):
    #     self.__Title = Title
    #
    # def set_description(self, Description):
    #     self.__Description =Description
    #
    # def set_creation_date(self, CreationDate):
    #     self.__CreationDate = CreationDate
    #
    # def set_medium(self, Medium):
    #     self.__Medium = Medium
    #
    # def set_image_url(self, ImageURL):
    #     self.__ImageURL = ImageURL
    #
    # def set_artist_id(self, ArtistID):
    #     self.__ArtistID = ArtistID



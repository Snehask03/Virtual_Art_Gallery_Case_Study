class Gallery:
    def __init__(self, gallery_id = None, gallery_name = None, gallery_description = None, gallery_location = None, curator_id = None, opening_hours = None, is_active = True):
        self.__gallery_id = gallery_id
        self.__gallery_name = gallery_name
        self.__gallery_description = gallery_description
        self.__gallery_location = gallery_location
        self.__curator_id = curator_id # foreign key (ArtistID)
        self.__opening_hours = opening_hours
        self.__is_active = is_active

    def __str__(self):
        return (
            f"Gallery [ID = {self.gallery_id}, Gallery Name = '{self.gallery_name}',\n"
            f"Description = '{self.gallery_description}', Location = '{self.gallery_location}',\n"
            f"Curator ID = {self.curator_id}, Opening Hours = '{self.opening_hours}', IS_Active = {self.is_active}]"
        )

    # Getters and Setters
    @property
    def gallery_id(self):
        return self.__gallery_id
    @gallery_id.setter
    def gallery_id(self, gallery_id):
        self.__gallery_id = gallery_id

    @property
    def gallery_name(self):
        return self.__gallery_name
    @gallery_name.setter
    def gallery_name(self, gallery_name):
        self.__gallery_name = gallery_name

    @property
    def gallery_description(self):
        return  self.__gallery_description
    @gallery_description.setter
    def gallery_description(self, gallery_description):
        self.__gallery_description = gallery_description

    @property
    def gallery_location(self):
        return self.__gallery_location
    @gallery_location.setter
    def gallery_location(self, gallery_location):
        self.__gallery_location = gallery_location

    @property
    def curator_id(self):
        return self.__curator_id
    @curator_id.setter
    def curator_id(self, curator_id):
        self.__curator_id = curator_id

    @property
    def opening_hours(self):
        return self.__opening_hours
    @opening_hours.setter
    def opening_hours(self, opening_hours):
        self.__opening_hours = opening_hours

    @property
    def is_active(self):
        return self.__is_active
    @is_active.setter
    def is_active(self, is_active):
        self.__is_active = is_active




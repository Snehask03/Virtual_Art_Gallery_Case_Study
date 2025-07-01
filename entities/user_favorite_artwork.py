class UserFavoriteArtwork:
    def __init__(self, user_id = None, artwork_id = None):
        self.__user_id = user_id
        self.__artwork_id = artwork_id

    def __str__(self):
        return (
            f"\nUser Favorite Artwork Information\n"
            f"User ID = {self.user_id},\n"
            f"Artwork ID = {self.artwork_id}\n"
        )
    # Getters and Setters
    @property
    def user_id(self):
        return self.__user_id
    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id

    @property
    def artwork_id(self):
        return self.__artwork_id
    @artwork_id.setter
    def artwork_id(self, artwork_id):
        self.__artwork_id = artwork_id



# Artist table exceptions
class ArtistNotFoundException(Exception):
    def __init__(self, message = "Artist does not exist!"):
        super().__init__(message)

class InvalidArtistIDException(Exception):
    def __init__(self, message="Invalid Artist ID has been entered!"):
        super().__init__(message)

class InvalidArtistNameException(Exception):
    def __init__(self, message="Invalid Artist name has been entered!"):
        super().__init__(message)

# Artwork not found exceptions:
class ArtworkNotFoundException(Exception):
    def __init__(self, message = "Artwork does not exist!"):
        super().__init__(message)

class InvalidArtworkIDException(Exception):
    def __init__(self, message = "Invalid Artwork ID has been entered!"):
        super().__init__(message)
        
class InvalidArtworkTitleException(Exception):
    def __init__(self, message = "Invalid Artwork Title has been entered!"):
        super().__init__(message)

# User not found exceptions:
class UserNotFoundException(Exception):
    def __init__(self, message = "User does not exist!"):
        super().__init__(message)

class InvalidUserIDException(Exception):
    def __init__(self, message="Invalid User ID has been entered!"):
        super().__init__(message)

class InvalidUserNameException(Exception):
    def __init__(self, message="Invalid username has been entered!"):
        super().__init__(message)

class InvalidUserPasswordException(Exception):
    def __init__(self, message="Invalid password has been entered!"):
        super().__init__(message)

# Gallery not found exceptions:
class GalleryNotFoundException(Exception):
    def __init__(self, message = "Gallery does not exist!"):
        super().__init__(message)

class InvalidGalleryIDException(Exception):
    def __init__(self, message="Invalid gallery ID has been entered!"):
        super().__init__(message)

class InvalidGalleryNameException(Exception):
    def __init__(self, message="Invalid gallery name has been entered!"):
        super().__init__(message)

#For User Favorite Artwork table
class DuplicateFavouriteEntryException(Exception):
    def __init__(self, message = "This entry already exists!"):
        super().__init__(message)

class FavoriteNotFoundException(Exception):
    def __init__(self, message = "The Favourite does not exists!"):
        super().__init__(message)

#For Artwork gallery table
class DuplicateArtworkGalleryMappingException(Exception):
    def __init__(self, message = "This artwork is already mapped to this gallery!"):
        super().__init__(message)

class MappingNotFoundException(Exception):
    def __init__(self, message = "The Mapping does not exists between artwork and gallery!"):
        super().__init__(message)

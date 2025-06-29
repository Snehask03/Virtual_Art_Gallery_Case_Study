from util.DBConnutil import DBConnUtil
from entities.artist import Artist
from entities.artwork import Artwork
from entities.gallery import Gallery
from entities.users import User
from exception.exceptions import InvalidArtistIDException, InvalidArtworkIDException, InvalidGalleryIDException,InvalidUserIDException, DuplicateArtworkGalleryMappingException, DuplicateFavouriteEntryException
from exception.exceptions import ArtistNotFoundException, ArtworkNotFoundException, GalleryNotFoundException, UserNotFoundException, MappingNotFoundException, FavoriteNotFoundException

class VirtualArtGalleryImpl:
    def __init__(self):
        self.connection = DBConnUtil.get_connection()

    # Artist Management:
    #Add a new artist:
    def add_artist(self, artist):
        cursor = None
        try:
            cursor = self.connection.cursor()
            insert_query = """
            INSERT INTO Artist(Name, Biography, Birth_Date, Nationality, Website, Contact_Information)
            VALUES(%s, %s, %s, %s, %s, %s)
            """
            values = (
                artist.name,
                artist.biography,
                artist.birth_date,
                artist.nationality,
                artist.website,
                artist.contact_information
            )
            cursor.execute(insert_query, values)
            self.connection.commit()
            artist.artist_id = cursor.lastrowid
            print(f"The Artist is added successfully!")
        except Exception as e:
            print("Error Adding the artist:", e)
            return None
        finally:
            if cursor:
                cursor.close()

    # Find an artist by their ID
    def find_artist(self, artist_id):
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Artist WHERE Artist_ID = %s"
            cursor.execute(query, (artist_id,))
            result = cursor.fetchone()
            if result:
                print(f"Here is the artist you're searching is given below:")
                return result
            else:
                raise InvalidArtistIDException
        except InvalidArtistIDException as e:
            print(f"Artist Error:{e}")
        except Exception as e:
            print("Unexpected error", e)
        finally:
            if cursor:
                cursor.close()

    # Search for artists with keyword
    def search_artists(self, keyword):
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Artist WHERE  Name LIKE %s or Biography LIKE %s or Nationality LIKE %s"
            keyword_result = f"%{keyword}%"
            cursor.execute(query, (keyword_result,keyword_result, keyword_result))
            results = cursor.fetchall()
            return results
        except ArtistNotFoundException as e:
            print(f"Artist Error:{e}")
        except Exception as e:
            print("Unexpected Error:", e)
        finally:
            if cursor:
                cursor.close()

    # Updating an artist details
    def update_artist(self, artist_id):
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Artist WHERE Artist_ID = %s", (artist_id,))
            current = cursor.fetchone()
            if not current:
                raise  InvalidArtistIDException
            print("If you want to keep the current value just click enter.\n")
            name = input(f"Enter the new name. The existing name is [{current[1]}]: ") or current[1]
            biography = input(f"Enter the new biography. The existing biography is [{current[2]}]: ") or current[2]
            birth_date = input(f"Enter the new birth date(YYYY-MM-DD). The existing birth date is [{current[3]}]: ") or current[3]
            nationality = input(f"Enter the new nationality. The existing nationality is [{current[4]}]: ") or current[4]
            website = input(f"Enter the new website. The existing website of the artist is [{current[5]}]: ") or current[5]
            contact_information = input(f"Enter the new contact information (email). The existing email is [{current[6]}]: ") or current[6]

            update_query = """
            UPDATE Artist
            SET Name = %s, Biography = %s, Birth_Date = %s, Nationality = %s, Website = %s, Contact_Information = %s
            WHERE Artist_ID = %s
            """
            values = (name, biography, birth_date, nationality, website, contact_information, artist_id)
            cursor.execute(update_query, values)
            self.connection.commit()
            if cursor.rowcount > 0:
                print("Artist updated successfully.")
            elif cursor.rowcount == 0:
                print("No changes made ")
            else:
                raise InvalidArtistIDException
        except InvalidArtistIDException as e:
            print(f"Artist Error:{e}")
        except Exception as e:
            print("Unexpected error:", e)
        finally:
            if cursor:
                cursor.close()

    #Deactivate a Artist:
    def deactivate_artist(self, artist_id):
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = """
            UPDATE Artist SET Is_Active = False WHERE Artist_ID = %s
            """
            cursor.execute(query, (artist_id,))
            self.connection.commit()
            if cursor.rowcount > 0:
                print("The artist is deactivated")
            else:
                raise ArtistNotFoundException

        except ArtistNotFoundException as e:
            print(f"Artist Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")
        finally:
            if cursor:
                cursor.close()

    # Removing an artist
    def remove_artist(self, artist_id):
        cursor = None
        try:
            if artist_id < 100 or artist_id > 199:
                raise InvalidArtistIDException
            cursor = self.connection.cursor()
            delete_query = """
            DELETE FROM Artist WHERE Artist_ID = %s
            """
            cursor.execute(delete_query, (artist_id,))
            self.connection.commit()
            if cursor.rowcount >0:
                print("The artist is removed from the table successfully")
            else:
                raise ArtistNotFoundException
        except ArtistNotFoundException as e:
            print(f"Artist Error:{e}")
        except Exception as e:
            print("Unexpected Error:", e)
        finally:
            if cursor:
                cursor.close()

    #Artwork Management:
    # Adding an artwork
    def add_artwork(self, artwork):
        cursor = None
        try:
            cursor = self.connection.cursor()
            insert_query = """
            INSERT INTO Artwork( Title, Description, Creation_Date, Medium, Image_URL, Artist_ID)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            values =(
                artwork.title,
                artwork.description,
                artwork.creation_date,
                artwork.medium,
                artwork.image_url,
                artwork.artist_id
            )
            cursor.execute(insert_query, values)
            self.connection.commit()
            artwork.artwork_id = cursor.lastrowid
            print("The artwork is added successfully!")
            return True
        except Exception as e:
            print("Error adding the artwork. Kindly check and try again", e)
            return False
        finally:
            if cursor:
                cursor.close()

    # Find the artwork by their ID
    def find_artwork(self, artwork_id):
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Artwork WHERE Artwork_ID = %s"
            cursor.execute(query, (artwork_id,))
            result = cursor.fetchone()
            if result:
                print(f"Here is the artwork you're searching is given below:")
                return result
            else:
                raise InvalidArtworkIDException
        except InvalidArtworkIDException as e:
            print(f"Artwork Error:{e}")
        except Exception as e:
            print(e)
        finally:
            if cursor:
                cursor.close()

    #Searching an artwork by some keyword
    def search_artworks(self, keyword):
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Artwork WHERE Title LIKE %s or Medium LIKE %s or Creation_Date LIKE %s"
            keyword_result = f"%{keyword}%"
            cursor.execute(query, (keyword_result, keyword_result, keyword_result))
            results = cursor.fetchall()
            return results
        except ArtworkNotFoundException as e:
            print(f"Artwork Error:{e}")
        except Exception as e:
            print("Unexpected Error:",e)
        finally:
            if cursor:
                cursor.close()

    # Updating an existing artwork
    def update_artwork(self, artwork_id):
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Artwork WHERE Artwork_ID = %s", (artwork_id,))
            current = cursor.fetchone()
            if not current:
                raise  InvalidArtworkIDException
            print("If you want to keep the current value just click enter.\n")
            title = input(f"Enter the new title. The existing title is  [{current[1]}]: ") or current[1]
            description = input(f"Enter the new description. The existing description is [{current[2]}]: ") or current[2]
            creation_date = input(f"Enter the new creation date(YYYY-MM-DD). The existing creation date is [{current[3]}]: ") or current[3]
            medium = input(f"Enter the new medium. The existing medium of the artwork is [{current[4]}]: ") or current[4]
            image_url = input(f"Enter the new image url. The existing image url is [{current[5]}]: ") or current[5]
            artist_id = input(f"If the artwork is linked to the wrong artist enter the right artist id here. The existing artist id is [{current[6]}] for your reference: ") or current[6]

            update_query = """
            UPDATE Artwork 
            SET Title = %s, Description = %s, Creation_Date = %s, Medium = %s, Image_URL = %s, Artist_ID = %s
            WHERE Artwork_ID = %s
            """
            values = (title, description, creation_date, medium, image_url, artist_id, artwork_id)
            cursor.execute(update_query, values)
            self.connection.commit()
            if cursor.rowcount > 0:
                print("Artwork updated successfully.")
                return True
            elif cursor.rowcount == 0:
                print("No changes made")
                return  False
            else:
                raise InvalidArtworkIDException
        except InvalidArtworkIDException as e:
            print(f"Artwork Error:{e}")
        except Exception as e:
            print("Unexpected error:", e)
            return False
        finally:
            if cursor:
                cursor.close()

    # Removing an artwork
    def remove_artwork(self, artwork_id):
        cursor = None
        try:
            if artwork_id < 200 or artwork_id > 299:
                raise InvalidArtworkIDException
            cursor = self.connection.cursor()
            delete_query = """
            DELETE FROM Artwork WHERE Artwork_ID = %s
            """
            cursor.execute(delete_query, (artwork_id,))
            self.connection.commit()
            if cursor.rowcount > 0:
                print("The artwork is removed from the table successfully")
                return True
            else:
                raise ArtworkNotFoundException
        except ArtistNotFoundException as e:
            print(f"Artwork Error:{e}")
            return False
        except Exception as e:
            print("Unexpected Error:", e)
        finally:
            if cursor:
                cursor.close()

    # Gallery Management:
    # Adding a Gallery
    def add_gallery(self, gallery):
        cursor = None
        try:
            cursor = self.connection.cursor()
            insert_query = """
            INSERT INTO Gallery(Gallery_Name, Gallery_Description, Gallery_Location, Curator_ID, Opening_Hours)
            VALUES(%s, %s, %s, %s, %s)
            """
            values = (
                gallery.gallery_name,
                gallery.gallery_description,
                gallery.gallery_location,
                gallery.curator_id,
                gallery.opening_hours
            )
            cursor.execute(insert_query, values)
            self.connection.commit()
            gallery.gallery_id = cursor.lastrowid
            print(f"The Gallery is added successfully!")
            return True
        except Exception as e:
            print("Error Adding the Gallery:", e)
            return False
        finally:
            if cursor:
                cursor.close()

    def find_gallery(self, gallery_id):
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Gallery WHERE Gallery_ID = %s"
            cursor.execute(query, (gallery_id,))
            result = cursor.fetchone()
            if result:
                print(f"Here is the gallery you're searching is given below:")
                return result
            else:
                raise InvalidGalleryIDException
        except InvalidGalleryIDException as e:
            print(f"Gallery Error:{e}")
        except Exception as e:
            print(e)
        finally:
            if cursor:
                cursor.close()

    def search_gallery(self, keyword):
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Gallery WHERE Gallery_Name LIKE %s or Curator_ID LIKE %s or Gallery_Location LIKE %s"
            keyword_result = f"%{keyword}%"
            cursor.execute(query, (keyword_result,keyword_result, keyword_result))
            results = cursor.fetchall()
            return results
        except GalleryNotFoundException as e:
            print(f"Gallery Error:{e}")
        except Exception as e:
            print("Unexpected Error:", e)
        finally:
            if cursor:
                cursor.close()

    # Updating an artist detail
    def update_gallery(self, gallery_id):
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Gallery WHERE Gallery_ID = %s", (gallery_id,))
            current = cursor.fetchone()
            if not current:
                raise InvalidGalleryIDException
            print("If you want to keep the current value just click enter.\n")
            gallery_name = input(f"Enter the new gallery name. The existing name is  [{current[1]}]: ") or current[1]
            gallery_description = input(f"Enter the new gallery description. The existing gallery description is [{current[2]}]: ") or current[2]
            gallery_location = input(f"Enter the new gallery location. The existing birth date is [{current[3]}]: ") or current[3]
            curator_id = input(f"Enter the new curator id (artist ID). The existing curator id (artist ID) is [{current[4]}]: ") or  current[4]
            opening_hours = input(f"Enter the updated opening hours. The existing opening hours of the gallery is [{current[5]}]: ") or current[5]
            update_query = """
            UPDATE Gallery
            SET Gallery_Name = %s, Gallery_Description = %s, Gallery_Location = %s, Curator_ID = %s, Opening_hours = %s
            WHERE Gallery_ID = %s
            """
            values = (gallery_name, gallery_description, gallery_location, curator_id, opening_hours,gallery_id)
            cursor.execute(update_query, values)
            self.connection.commit()
            if cursor.rowcount > 0:
                print("Gallery updated successfully.")
                return True
            elif cursor.rowcount == 0:
                print("No changes made")
                return False
            else:
                raise InvalidGalleryIDException
        except InvalidGalleryIDException as e:
            print(f"Gallery Error:{e}")
        except Exception as e:
            print("Unexpected error:", e)
        finally:
            if cursor:
                cursor.close()

    # Deactivate a Gallery:
    def deactivate_gallery(self, gallery_id):
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = """
            UPDATE Gallery SET Is_Active = False WHERE Gallery_ID = %s
            """
            cursor.execute(query, (gallery_id,))
            self.connection.commit()
            if cursor.rowcount > 0:
                print("The Gallery is deactivated")
            else:
                raise GalleryNotFoundException
        except GalleryNotFoundException as e:
            print(f"Gallery Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")
        finally:
            if cursor:
                cursor.close()

    # Removing an gallery
    def remove_gallery(self, gallery_id):
        cursor = None
        try:
            if gallery_id < 300 or gallery_id > 399:
                raise InvalidArtistIDException
            cursor = self.connection.cursor()
            delete_query = """
            DELETE FROM Gallery WHERE Gallery_ID = %s
            """
            cursor.execute(delete_query, (gallery_id,))
            self.connection.commit()
            if cursor.rowcount > 0:
                print("The gallery is removed from the table successfully")
                return True
            else:
                raise GalleryNotFoundException
        except GalleryNotFoundException as e:
            print(f"Gallery Error:{e}")
        except Exception as e:
            print("Unexpected Error:", e)
        finally:
            if cursor:
                cursor.close()

    #User Management
    # Add a new user:
    def add_user(self, user):
        cursor = None
        try:
            cursor = self.connection.cursor()
            insert_query = """
            INSERT INTO Users(User_Name, User_Password, Email, First_Name, Last_Name,Date_Of_Birth, Profile_Picture)
            VALUES(%s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                user.user_name,
                user.user_password,
                user.email,
                user.first_name,
                user.last_name,
                user.date_of_birth,
                user.profile_picture
            )
            cursor.execute(insert_query, values)
            self.connection.commit()
            user.user_id = cursor.lastrowid
            print(f"The User is added successfully!")
        except Exception as e:
            print("Error Adding the User:", e)
            return None
        finally:
            if cursor:
                cursor.close()

    # Find an user by their ID
    def find_user(self, user_id):
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Users WHERE User_ID = %s"
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()
            if result:
                print(f"Here is the user you're searching is given below:")
                return result
            else:
                raise InvalidUserIDException
        except InvalidUserIDException as e:
            print(f"User Error:{e}")
        except Exception as e:
            print("Unexpected error", e)
        finally:
            if cursor:
                cursor.close()

    # Search for users with keyword
    def search_user(self, keyword):
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Users WHERE User_Name LIKE %s or First_Name LIKE %s or Email LIKE %s"
            keyword_result = f"%{keyword}%"
            cursor.execute(query, (keyword_result, keyword_result, keyword_result))
            results = cursor.fetchall()
            return results
        except UserNotFoundException as e:
            print(f"User Error:{e}")
        except Exception as e:
            print("Unexpected Error:", e)
        finally:
            if cursor:
                cursor.close()

    # Updating an user details
    def update_user(self, user_id):
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Users WHERE User_ID = %s", (user_id,))
            current = cursor.fetchone()
            if not current:
                raise InvalidUserIDException
            print("If you want to keep the current value just click enter.\n")
            user_name = input(f"Enter the new name. The existing name is [{current[1]}]: ") or current[1]
            user_password = input(f"Enter the new password : ") or current[2]
            email = input(f"Enter the new email. The existing email is [{current[3]}]: ") or current[3]
            first_name = input(f"Enter your first name. The existing first name is [{current[4]}]: ") or current[4]
            last_name = input(f"Enter the new last name. The existing last name is [{current[5]}]: ") or current[5]
            date_of_birth = input(f"Enter your date of birth (YYYY-MM-DD). The existing date of birth is [{current[6]}]: ") or current[6]
            profile_picture = input(f"Enter image link to set your profile picture. Your existing profile picture is [{current[7]}]: ") or current[7]

            update_query = """
            UPDATE Users
            SET User_Name = %s, User_Password = %s, Email = %s, First_Name = %s, Last_Name = %s, Date_Of_Birth = %s, Profile_Picture = %s 
            WHERE User_ID = %s
            """
            values = (user_name, user_password, email, first_name, last_name, date_of_birth, profile_picture, user_id)
            cursor.execute(update_query, values)
            self.connection.commit()
            if cursor.rowcount > 0:
                print("User updated successfully.")
            elif cursor.rowcount == 0:
                print("No changes made")
            else:
                raise InvalidUserIDException
        except InvalidUserIDException as e:
            print(f"User Error:{e}")
        except Exception as e:
            print("Unexpected error:", e)
        finally:
            if cursor:
                cursor.close()

    def deactivate_user(self, user_id):
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = """
            UPDATE Users SET Is_Active = False WHERE User_ID = %s
            """
            cursor.execute(query, (user_id,))
            self.connection.commit()
            if cursor.rowcount > 0:
                print("The User is deactivated")
            else:
                raise UserNotFoundException
        except UserNotFoundException as e:
            print(f"User Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")
        finally:
            if cursor:
                cursor.close()

    # Removing an user
    def remove_user(self, user_id):
        cursor = None
        try:
            if user_id < 400 or user_id > 499:
                raise InvalidUserIDException
            cursor = self.connection.cursor()
            delete_query = """
            DELETE FROM Users WHERE User_ID = %s
            """
            cursor.execute(delete_query, (user_id,))
            self.connection.commit()
            if cursor.rowcount > 0:
                print("The User is removed from the table successfully")
            else:
                raise UserNotFoundException
        except UserNotFoundException as e:
            print(f"User Error:{e}")
        except Exception as e:
            print("Unexpected Error:", e)
        finally:
            if cursor:
                cursor.close()

    # Artwork Gallery Junction Table
    def add_artwork_to_gallery(self, artwork_id, gallery_id):
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO ArtworkGallery(Artwork_ID, Gallery_ID) VALUES(%s, %s)"
            cursor.execute(query, (artwork_id, gallery_id))
            self.connection.commit()
            print("Artwork has been added successfully to the gallery")
            return True
        except DuplicateArtworkGalleryMappingException as e:
            print(f"Artwork Gallery Error: {e}")
            return False
        except Exception as e:
            print(f"Unexpected Error: {e}")
            return False
        finally:
            if cursor:
                cursor.close()

    def get_artworks_by_gallery(self, gallery_id):
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = """
            SELECT a.Artwork_ID, a.Title, a.Description
            FROM Artwork a
            JOIN ArtworkGallery ag ON a.Artwork_ID = ag.Artwork_ID
            WHERE ag.Gallery_ID = %s
            """
            cursor.execute(query, (gallery_id,))
            results = cursor.fetchall()
            return results
        except MappingNotFoundException as e:
            print(f"Artwork Gallery Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

    def get_galleries_by_artwork(self, artwork_id):
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = """
            SELECT g.Gallery_ID, g.Gallery_Name, g.Location
            FROM Gallery g
            JOIN ArtworkGallery ag ON g.Gallery_ID = ag.Gallery_ID
            WHERE ag.Artwork_ID = %s 
            """
            cursor.execute(query, (artwork_id,))
            results = cursor.fetchall()
            return results
        except MappingNotFoundException as e:
            print(f"Artwork Gallery Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

    def remove_artwork_from_gallery(self, artwork_id, gallery_id):
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = """
            DELETE FROM ArtworkGallery WHERE Artwork_ID = %s AND Gallery_ID = %s
            """
            cursor.execute(query, (artwork_id, gallery_id))
            self.connection.commit()
            if cursor.rowcount > 0:
                print("Artwork removed successfully from the gallery.")
                return True
            elif cursor.rowcount == 0:
                print("No changes made")
                return False
            else:
                raise MappingNotFoundException
        except MappingNotFoundException as e:
            print(f"Artwork Gallery Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")
        finally:
            if cursor:
                cursor.close()

    #User Favorites Junction Table:
    def add_artwork_to_favourite(self, user_id, artwork_id):
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = """
            INSERT INTO UserFavoriteArtwork (User_ID, Artwork_ID)
            VALUES(%s, %s)
            """
            cursor.execute(query,(user_id, artwork_id))
            self.connection.commit()
            print("Artwork added to favorites.")
            return True
        except DuplicateFavouriteEntryException as e:
            print(f"User Favorite Artwork Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")
        finally:
            if cursor:
                cursor.close()

    def remove_artwork_from_favourite(self, user_id, artwork_id):
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = """
            DELETE FROM UserFavoriteArtwork WHERE User_ID = %s AND Artwork_ID = %s
            """
            cursor.execute(query, (user_id, artwork_id))
            self.connection.commit()
            if cursor.rowcount > 0:
                print("Artwork removed successfully from the favorites.")
                return True
            elif cursor.rowcount == 0:
                print("No changes made")
                return False
            else:
                raise FavoriteNotFoundException
        except FavoriteNotFoundException as e:
            print(f"User Favourite Artwork Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")
        finally:
            if cursor:
                cursor.close()
    def get_user_favourite_artworks(self, user_id):
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = """
            SELECT a.Artwork_ID, a.Title, a.Description
            FROM Artwork a
            JOIN UserFavoriteArtwork uf ON a.Artwork_ID = uf.Artwork_ID
            WHERE uf.User_ID = %s
            """
            cursor.execute(query, (user_id,))
            results = cursor.fetchall()
            return results
        except FavoriteNotFoundException as e:
            print(f"User Favorite Artwork Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")
        finally:
            if cursor:
                cursor.close()



if __name__ == "__main__":
    service = VirtualArtGalleryImpl()
    # artwork = Artwork(
    #     title= "Fall among silence",
    #     description="A digital representation of silent landscapes",
    #     creation_date="2015-05-24",
    #     medium="Digital",
    #     image_url="https://Fall among silence.com",
    #     artist_id = 102
    # )
    # service.add_artwork(artwork)
    # print(service.find_artwork(201))
    #service.update_artwork(201)
    # service.update_artist(101)
    # gallery = Gallery(
    #     gallery_name= "Smith Inc",
    #     gallery_description="Features abstract landscapes and brush works by emerging artists.",
    #     gallery_location="West Jason",
    #     curator_id=101,
    #     opening_hours="9 AM onwards"
    # )
    # service.add_gallery(gallery)
    # print(service.find_gallery(301))
    # user = User(
    #     user_name= "olivia82",
    #     user_password= "'olivia_82",
    #     email= "oliviauser@gmail.com",
    #     first_name= "Olivia",
    #     last_name= "Liam",
    #     date_of_birth="1982-06-02",
    #     profile_picture="oliviadrive.jpg"
    # )
    # service.add_user(user)
    # print(service.find_user(401))
    print(service.search_user("olivia"))


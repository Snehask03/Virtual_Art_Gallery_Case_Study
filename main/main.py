from tabulate import tabulate
from dao.VirtualArtGalleryImpl import VirtualArtGalleryImpl
from entities.artist import Artist
from entities.artwork import Artwork
from entities.gallery import Gallery
from entities.users import User
from entities.artwork_gallery import ArtworkGallery
from entities.user_favorite_artwork import UserFavoriteArtwork
from exception.exceptions import DuplicateFavouriteEntryException, DuplicateArtworkGalleryMappingException
from exception.exceptions import MappingNotFoundException, FavoriteNotFoundException
from exception.exceptions import InvalidArtistIDException
from exception.exceptions import ArtistNotFoundException
from exception.exceptions import ArtworkNotFoundException
from exception.exceptions import InvalidArtworkIDException
from exception.exceptions import InvalidGalleryIDException
from exception.exceptions import GalleryNotFoundException
from exception.exceptions import UserNotFoundException
from exception.exceptions import InvalidUserIDException

service = VirtualArtGalleryImpl()
def artist_menu(service):
    while True:
        print("\nWelcome to the Artist Management Section!")
        print("\n ---Artist Menu---")
        print("1.Add Artist")
        print("2.Find an artist by ID")
        print("3.Search Artist")
        print("4.Update Artist")
        print("5.Deactivate Artist")
        print("6.Remove Artist")
        print("7.View all Artists")
        print("8.Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the artist name: ")
            biography = input("Enter the biography of the artist: ")
            birth_date = input("Enter birth date (YYYY-MM-DD): ")
            nationality = input("Enter the artist's nationality: ")
            website = input("Enter the website of the artist: ")
            contact_information = input("Enter contact_information(email) of the artist: ")
            artist = Artist(name = name, biography = biography, birth_date = birth_date, nationality = nationality,website = website, contact_information = contact_information)
            service.add_artist(artist)
        elif choice == '2':
            artist_id = int(input("Enter the Artist ID: "))
            try:
                result = service.find_artist(artist_id)
                print(result)
            except ArtistNotFoundException as e:
                print(f"Artist Error: {e}")
            except InvalidArtistIDException as e:
                print(f"Artist Error: {e}")
        elif choice == '3':
            try:
                keyword = input("Enter the keyword (name, nationality, biography) related to the artist: ")
                result = service.search_artists(keyword)
                if result:
                    print(f"The Artists that match your keyword is given below: ")
                    for r in result:
                        print(r)
                else:
                    print("No matches found")
            except ArtistNotFoundException as e:
                print(f"Artist Error: {e}")

        elif choice == '4':
            artist_id = int(input("Enter the Artist ID: "))
            try:
                service.update_artist(artist_id)
            except ArtistNotFoundException as e:
                print(f"Artist Error: {e}")
            except InvalidArtistIDException as e:
                print(f"Artist Error: {e}")

        elif choice == '5':
            artist_id = int(input("Enter the Artist ID to deactivate: "))
            service.deactivate_artist(artist_id)

        elif choice == '6':
            artist_id = int(input("Enter the Artist ID you want to remove: "))
            try:
                confirm = input("Are you sure you want to delete this artist?(y/n): ")
                if confirm.lower() == 'y':
                    service.remove_artist(artist_id)
                else:
                    print("Deletion cancelled")
            except ArtistNotFoundException as e:
                print(f"Artist Error: {e}")
            except InvalidArtistIDException as e:
                print(f"Artist Error: {e}")

        elif choice == '7':
            artists = service.view_all_artists()
            if artists:
                table = [[a[0], a[1], a[2], a[3], a[4], a[5], a[6]] for a in artists]
                print(tabulate(table, headers=["Artist_ID", "Name", "Biography", "Birth_Date", "Nationality", "Website",
                                               "Contact_Information"], tablefmt="grid"))
            else:
                print("No artists Found")
        elif choice == '8':
            break
        else:
            print("Invalid input. Please try again")

def artwork_menu(service):
    while True:
        print("\nWelcome to the Artwork Management Section!")
        print("\n ---Artwork Menu---")
        print("1.Add Artwork")
        print("2.Find an artwork by ID")
        print("3.Search Artwork")
        print("4.Update Artwork")
        print("5.Remove Artwork")
        print("6.View all artworks")
        print("7.Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the artwork title: ")
            description = input("Enter the description of the artwork: ")
            creation_date = input("Enter creation date (YYYY-MM-DD): ")
            medium = input("Enter the artwork medium: ")
            image_url = input("Enter the image url of the artwork: ")
            artist_id = int(input("Enter the id of the artist of the artwork:"))
            artwork = Artwork(title = title, description = description, creation_date = creation_date, medium = medium, image_url = image_url, artist_id = artist_id)
            service.add_artwork(artwork)
        elif choice == '2':
            artwork_id = int(input("Enter the Artwork ID: "))
            try:
                result = service.find_artwork(artwork_id)
                print(result)
            except ArtworkNotFoundException as e:
                print(f"Artwork Error: {e}")
            except InvalidArtworkIDException as e:
                print(f"Artwork Error: {e}")
        elif choice == '3':
            try:
                keyword = input("Enter the keyword (title, medium or creation date (YYYY-MM-DD)) related to the artist: ")
                result = service.search_artworks(keyword)
                if result:
                    print(f"The Artworks that match your keyword is given below: ")
                    for r in result:
                        print(r)
                else:
                    print("No matches found")
            except ArtworkNotFoundException as e:
                print(f"Artwork Error: {e}")
        elif choice == '4':
            artwork_id = int(input("Enter the Artwork ID: "))
            try:
                service.update_artwork(artwork_id)
            except ArtworkNotFoundException as e:
                print(f"Artwork Error: {e}")
            except InvalidArtworkIDException as e:
                print(f"Artwork Error: {e}")
        elif choice == '5':
            artwork_id = int(input("Enter the Artwork ID you want to remove: "))
            try:
                confirm = input("Are you sure you want to delete this artwork?(y/n): ")
                if confirm.lower() == 'y':
                    service.remove_artwork(artwork_id)
                else:
                    print("Deletion Cancelled")
            except ArtworkNotFoundException as e:
                print(f"Artwork Error: {e}")
            except InvalidArtworkIDException as e:
                print(f"Artwork Error: {e}")

        elif choice == '6':
            artworks = service.view_all_artworks()
            if artworks:
                table = [[a[0], a[1], a[2], a[3], a[4], a[5], a[6]] for a in artworks]
                print(tabulate(table,
                               headers=["Artwork_ID", "Title", "Description", "Creation_Date", "Medium", "Image_URL",
                                        "Artist_ID"], tablefmt="grid"))
            else:
                print("No Artworks Found")
        elif choice == '7':
            break
        else:
            print("Invalid input. Please try again")

def gallery_menu(service):
    while True:
        print("\nWelcome to the Gallery Management Section!")
        print("\n ---Gallery Menu---")
        print("1.Add Gallery")
        print("2.Find a gallery by ID")
        print("3.Search gallery")
        print("4.Update gallery")
        print("5.Deactivate gallery")
        print("6.Remove gallery")
        print("7.View all galleries")
        print("8.Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the gallery name: ")
            description = input("Enter the description of the gallery: ")
            location = input("Enter gallery location: ")
            curator_id = int(input("Enter the id of the artist of the gallery: "))
            opening_hours = input("Enter the opening hours (like 9 AM onwards) of the gallery: ")
            gallery = Gallery(gallery_name = name, gallery_description = description, gallery_location = location, curator_id = curator_id, opening_hours = opening_hours)
            service.add_gallery(gallery)
        elif choice == '2':
            gallery_id = int(input("Enter the Gallery ID: "))
            try:
                result = service.find_gallery(gallery_id)
                print(result)
            except GalleryNotFoundException as e:
                print(f"Gallery Error: {e}")
            except InvalidGalleryIDException as e:
                print(f"Gallery Error: {e}")
        elif choice == '3':
            try:
                keyword = input("Enter the keyword (name, location or the curator id) related to the artist: ")
                result = service.search_gallery(keyword)
                if result:
                    print(f"The Gallery that match your keyword is given below: ")
                    for r in result:
                        print(r)
                else:
                    print("No matches found")
            except GalleryNotFoundException as e:
                print(f"Gallery Error: {e}")
        elif choice == '4':
            gallery_id = int(input("Enter the Gallery ID: "))
            try:
                service.update_gallery(gallery_id)
            except GalleryNotFoundException as e:
                print(f"Gallery Error: {e}")
            except InvalidGalleryIDException as e:
                print(f"Gallery Error: {e}")

        elif choice == '5':
            gallery_id = int(input("Enter the gallery ID to deactivate: "))
            service.deactivate_gallery(gallery_id)

        elif choice == '6':
            gallery_id = int(input("Enter the gallery ID you want to remove: "))
            try:
                confirm = input("Are you sure you want to delete this gallery?(y/n): ")
                if confirm.lower() == 'y':
                    service.remove_gallery(gallery_id)
                else:
                    print("Deletion Cancelled")
            except GalleryNotFoundException as e:
                print(f"Gallery Error: {e}")
            except InvalidGalleryIDException as e:
                print(f"Gallery Error: {e}")

        elif choice == '7':
            galleries = service.view_all_galleries()
            if galleries:
                table = [[g[0], g[1], g[2], g[3], g[4], g[5]] for g in galleries]
                print(tabulate(table, headers=["Gallery_ID", "Gallery_Name", "Gallery_Description", "Gallery_Location",
                                               "Curator", "Opening_Hours"], tablefmt="grid"))
            else:
                print("No Galleries found")
        elif choice == '8':
            print("Exit")
            break
        else:
            print("Invalid input. Please try again")

def user_menu(service):
    while True:
        print("\nWelcome to the User Management Section!")
        print("\n ---User Menu---")
        print("1.Add User")
        print("2.Find a user by ID")
        print("3.Search User")
        print("4.Update User")
        print("5.Deactivate User")
        print("6.Remove User")
        print("7.Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            user_name = input("Enter the user name: ")
            user_password = input("Enter the password you want to set: ")
            email = input("Enter your email: ")
            first_name = input("Enter the first name: ")
            last_name = input("Enter your last name: ")
            date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")
            profile_picture = input("Enter the image link to your profile picture: ")
            user = User(user_name = user_name, user_password = user_password, email = email, first_name = first_name, last_name = last_name, date_of_birth = date_of_birth, profile_picture = profile_picture)
            service.add_user(user)
        elif choice == '2':
            user_id = int(input("Enter the User ID: "))
            try:
                result = service.find_user(user_id)
                print(result)
            except UserNotFoundException as e:
                print(f"User Error: {e}")
            except InvalidUserIDException as e:
                print(f"User Error: {e}")
        elif choice == '3':
            try:
                keyword = input("Enter the keyword (username, first name, email) related to the user: ")
                result = service.search_user(keyword)
                if result:
                    print(f"The Users that match your keyword is given below:")
                    for r in result:
                        print(r)
                else:
                    print("No matches found")
            except UserNotFoundException as e:
                print(f"User Error: {e}")

        elif choice == '4':
            user_id = int(input("Enter the User ID: "))
            try:
                service.update_user(user_id)
            except UserNotFoundException as e:
                print(f"User Error: {e}")
            except InvalidUserIDException as e:
                print(f"User Error: {e}")

        elif choice == '5':
            user_id = int(input("Enter the user ID to deactivate: "))
            service.deactivate_user(user_id)

        elif choice == '6':
            user_id = int(input("Enter the User ID you want to remove: "))
            try:
                confirm = input("Are you sure you want to delete this user?(y/n): ")
                if confirm.lower() == 'y':
                    service.remove_user(user_id)
                else:
                    print("Deletion cancelled")
            except UserNotFoundException as e:
                print(f"User Error: {e}")
            except InvalidUserIDException as e:
                print(f"User Error: {e}")

        elif choice == '7':
            break
        else:
            print("Invalid input. Please try again")

def artwork_gallery_menu(service):
    while True:
        print("\n --- Artwork Gallery Management Section ---")
        print("1.Add Artwork to the Gallery")
        print("2.Remove Artwork from Gallery")
        print("3.View all Artwork Gallery Mapping")
        print("4.Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            artwork_id =int(input("Enter Artwork ID to add: "))
            gallery_id = int(input("Enter the Gallery ID to map with: "))
            service.add_artwork_to_gallery(artwork_id, gallery_id)

        elif choice == '2':
            artwork_id = int(input("Enter Artwork ID to add: "))
            gallery_id = int(input("Enter the Gallery ID to remove from: "))
            service.remove_artwork_from_gallery(artwork_id, gallery_id)

        elif choice == '3':
            gallery_id = int(input("Enter the gallery id: "))
            mappings = service.get_artworks_by_gallery(gallery_id)
        elif choice == '4':
            break
        else:
            print("Invalid Input. Please try again.")

def user_favorite_menu(service):
    while True:
        print("\n --- User Favorite Management system ---")
        print("1.Add artwork to Favorites")
        print("2.Remove Artwork from the User Favorite")
        print("3.View User's favorite Artworks")
        print("4.Update User favorite")
        print("5.Back to Main menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            user_id = int(input("Enter the user id: "))
            artwork_id = int(input("Enter artwork id to add to favorites: "))
            service.add_artwork_to_favourite(user_id, artwork_id)

        elif choice == '2':
            user_id = int(input("Enter the user id: "))
            artwork_id = int(input("Enter artwork id to remove from favorites: "))
            service.remove_artwork_from_favourite(user_id, artwork_id)
        elif choice == '3':
            user_id = int(input("Enter user id to view their favourites: "))
            artworks = service.get_user_favourite_artworks(user_id)
            if artworks:
                headers = ["Artwork_ID", "Title"]
                table = [[a[0], a[1]] for a in artworks]
                print(f"Favorite artworks for the user id {user_id}: ")
                print(tabulate(table, headers= headers, tablefmt="grid"))
            else:
                print("No favorites found")
        elif choice =='4':
            user_id = int(input("Enter the user id: "))
            old_artwork_id = int(input("Enter the old artwork id to update: "))
            new_artwork_id = int(input("Enter the new artwork id to set as favorites: "))
            service.update_favorites_artwork(user_id, old_artwork_id, new_artwork_id)

        elif choice == '5':
            break
        else:
            print("Invalid input. Please try again.")

def main():
    while True:
        print("Welcome to the Virtual Art Gallery System")
        print("1.New User Registration:")
        print("2.Existing User Login:")
        print("3.You are artist or Want to be a artist and add artwork?chose this")
        print("4.Exit:")

        choice = input("Enter your choice:")
        if choice == '1':
            print("\n --- User Registration---")
            user_name = input("Enter your user name:")
            user_password = input("Enter your password:")
            email = input("Enter your email:")
            first_name = input("Enter your first name:")
            last_name = input("Enter your last name: ")
            date_of_birth = input("Enter your date of birth(YYYY-MM-DD):")
            profile_picture = input("Enter the link to your profile picture:")
            role = input("Enter your role:")
            if role not in ['admin', 'user']:
                print("Invalid Role entered.Default role is user.")
                role = 'user'
            user = User(user_name = user_name, user_password= user_password, email= email, first_name = first_name, last_name=last_name, date_of_birth=date_of_birth, profile_picture=profile_picture, role=role)
            service.add_user(user)
            print(f"Registration successful! Your User ID is {user.user_id}")
        elif choice == '2':
            user_name = input("Enter your username: ")
            user_password = input("Enter your password: ")
            try:
                user = service.validate_user(user_name, user_password)
                if user is None:
                    print("Invalid username or password")
                    continue

                if user.role.lower() =='admin':
                    print(f"\n Welcome Admin {user.first_name}! | (User ID : {user.user_id})\n")
                    while True:
                        print("\n--- Admin Main Menu---")
                        print("a. Artist Management Section")
                        print("b. Artwork Management Section")
                        print("c. Gallery Management Section")
                        print("d. User Management Section")
                        print("e. User Favorites Management Section")
                        print("f. Artwork Gallery Management Section")
                        print("g. Logout")

                        choice = input("Enter your choice: ")

                        if choice.lower() == "a":
                            artist_menu(service)
                        elif choice.lower() == "b":
                            artwork_menu(service)
                        elif choice.lower() == "c":
                            gallery_menu(service)
                        elif choice.lower() == "d":
                            user_menu(service)
                        elif choice.lower() == "e":
                            user_favorite_menu(service)
                        elif choice.lower() == "f":
                            artwork_gallery_menu(service)
                        elif choice.lower() == "g":
                            print("Logging out")
                            break
                        else:
                            print("Invalid input. Please try again ")
                else:
                    print(f"\n Welcome {user.first_name}! | (User ID : {user.user_id})")
                    while True:
                        print("\n --- User Main Menu---")
                        print("1.Update your profile")
                        print("2.View or update favorites")
                        print("3.Browse Artworks")
                        print("4.Browse Artists")
                        print("5.Browse Galleries")
                        print("6.Browse Artwork-Gallery Mapping")
                        print("7.View all artworks")
                        print("8.View all artists")
                        print("9.View all galleries")
                        print("10.View all artwork-gallery mappings")
                        print("11.Logout")

                        choice = input("Enter your choice: ")

                        if choice == '1':
                            service.update_user(user.user_id)
                        elif choice == '2':
                            user_favorite_menu(service)
                        elif choice == '3':
                            try:
                                keyword = input("Enter artwork Keyword (Title, Medium, or Creation date): ")
                                results = service.search_artworks(keyword)
                                for r in results:
                                    print(r)
                            except ArtworkNotFoundException as e:
                                print(f"Error: {e}")
                        elif choice == '4':
                            try:
                                keyword = input("Enter the artists keyword (name, nationality, bio): ")
                                results = service.search_artists(keyword)
                                for r in results:
                                    print(r)
                            except ArtistNotFoundException as e:
                                print(f"Error: {e}")
                        elif choice == '5':
                            try:
                                keyword = input("Enter the gallery keyword (name, location, curator id): ")
                                results = service.search_gallery(keyword)
                                for r in results:
                                    print(r)
                            except GalleryNotFoundException as e:
                                print(f"Error : {e}")
                        elif choice == '6':
                            gallery_id = int(input("Enter gallery ID to see artworks mapped: "))
                            mappings = service.get_artworks_by_gallery(gallery_id)
                            if mappings:
                                for m in mappings:
                                    print(f"Artwork ID : {m[0]} <--> Gallery ID: {m[1]}")
                            else:
                                print("No mappings found")
                        elif choice == '7':
                            artworks = service.view_all_artworks()
                            if artworks:
                                table = [[a[0], a[1], a[2], a[3], a[4], a[5], a[6]] for a in artworks]
                                print(tabulate(table, headers=["Artwork_ID", "Title", "Description", "Creation_Date", "Medium","Image_URL","Artist_ID"], tablefmt="grid"))
                            else:
                                print("No Artworks Found")
                        elif choice == '8':
                            artists = service.view_all_artists()
                            if artists:
                                table = [[a[0],a[1], a[2], a[3], a[4], a[5], a[6]]for a in artists]
                                print(tabulate(table, headers=["Artist_ID", "Name", "Biography", "Birth_Date", "Nationality", "Website","Contact_Information"], tablefmt="grid"))
                            else:
                                print("No artists Found")
                        elif choice == '9':
                            galleries = service.view_all_galleries()
                            if galleries:
                                table = [[g[0], g[1], g[2], g[3], g[4], g[5]] for g in galleries]
                                print(tabulate(table, headers=["Gallery_ID", "Gallery_Name", "Gallery_Description", "Gallery_Location","Curator", "Opening_Hours" ], tablefmt="grid"))
                            else:
                                print("No Galleries found")
                        elif choice == '10':
                            artwork_gallery_mappings = service.view_all_artwork_gallery_mappings()
                        elif choice == '11':
                            print("Logging Out")
                            break
                        else:
                            print("Invalid input. Please try again.")

            except (UserNotFoundException, InvalidUserIDException) as e:
                print(f"Login Error: {e}")
            except ValueError:
                print("Invalid Input!")

        elif choice == '3':
            print("\n --- Artist Login ---")
            print("1.login")
            print("2.New Artist")
            choice = input("Enter your choice: ")
            if choice == '2':
                name = input("Enter the artist name: ")
                biography = input("Enter the biography of the artist: ")
                birth_date = input("Enter birth date (YYYY-MM-DD): ")
                nationality = input("Enter the artist's nationality: ")
                website = input("Enter the website of the artist: ")
                contact_information = input("Enter contact_information(email) of the artist: ")
                artist = Artist(
                    name=name,
                    biography=biography,
                    birth_date=birth_date,
                    nationality=nationality,
                    website=website,
                    contact_information=contact_information)
                service.add_artist(artist)
                print(f"Artist Registration successful | Artist ID is {artist.artist_id}")

            elif choice == '1':
                name = input("Enter your name: ")
                birth_date = input("Enter your birthdate (YYYY-MM-DD): ")
                try:
                    artist = service.validate_artist(name, birth_date)
                    if artist:
                        print(f"\n Welcome Artist {artist.name} | Artist ID {artist.artist_id}")
                        while True:
                            print("\n--- Artist Menu ---")
                            print("1.Add your artwork")
                            print("2.View your artworks")
                            print("3.logout")
                            choice = input("Enter your choice: ")
                            if choice == '1':
                                title = input("Enter the artwork title: ")
                                description = input("Enter the description of the artwork: ")
                                creation_date = input("Enter creation date (YYYY-MM-DD): ")
                                medium = input("Enter the artwork medium: ")
                                image_url = input("Enter the image url of the artwork: ")
                                artist_id = int(input("Enter the id of the artist of the artwork:"))
                                artwork = Artwork(title=title, description=description, creation_date=creation_date, medium=medium,
                                                  image_url=image_url, artist_id=artist_id)
                                service.add_artwork(artwork)
                                print(f" Artwork is added succesfully | Artwork ID is {artwork.artwork_id}")
                            elif choice == '2':
                                artworks = service.view_artworks_by_artist(artist.artist_id)
                                if artworks:
                                    table = [[a.artwork_id, a.title, a.medium, a.creation_date, a.image_url, a.artist_id] for a in artworks]
                                    print(tabulate(table, headers=["Artwork_ID", "Title", "Medium", "Creation_Date",
                                                                   "Image_URL", "Artist_ID"], tablefmt="grid"))
                                else:
                                    print("No Artworks Found")
                            elif choice == '3':
                                print("Logging out")
                                break
                            else:
                                print("Invalid Choice")
                except Exception as e:
                    print(f"Error:", e)
        elif choice == '4':
            print("Thanks for visiting the virtual art gallery")
            break
        else:
            print("Invalid Input!")

if __name__ == "__main__":
    main()

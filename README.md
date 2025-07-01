# Virtual Art Gallery System

An interactive and immersive system for exploring, managing, and appreciating a diverse collection of artworks. This is completely built using Python and MySQL and ensures OOPS, DAO, and layered Architecture principles. 
**This project goes beyond CRUD - Offering a fully modular layered, and role-sensitive CLI Experience for managing a virtual art gallery using real-world business logics**

## Architectures:
- **Entity Layer**: Contains classes like Artist, Artwork, Gallery, User, UserFavoriteArtwork, ArtworkGallery(Artwork-Gallery mapping)
- **DAO Layer**: Interfaces and their implementations for clean DB Interaction
- **Util Layer**: Handles secure database connections and utility functions
- **Main Module**: Contains the menu logic for a smooth user interface

## Features

**Role-Based Access System**:
- Three user types: Admin, Registered users, and Artists.
- Admins: Full access to all system features
- Users: Can manage profiles, search/browse/view artworks, and manage favorites.
- Artists: Can register/login separately to upload and manage their own artworks.

**Artist Management**: 
- Create and manage artists with additional functionalities.
- Add the artist, search for artists using keywords, remove, and update artists.
- Soft deletion of the artist is available through the deactivation of the artist
- View all registered artists in a clean tabular format
  
**Artwork Management**: 
- Manage the artwork information 
- This enables to addition, update, deletion, and also search for artworks using a keyword.
- Artist can upload and view their own artworks.
- Users can browse all artworks in tabular view.

**Gallery Management**:
- Create and manage galleries with their curators assignment.
- This also has additional functionalities like update, delete, and search for galleries using a keyword.
- View all galleries in the tabular format
  
**User Management**:
- User registration and management functions.
- A new user can enter their role to get access accordingly
- Contains all the user details, enables update, delete, and search users using keyword functions.
- User can also add their favorite artworks for future reference.
- Users can add, view, update, and remove their favorite artworks
  
**Artwork-Gallery Mapping**: 
- This system also allows you to map artworks to the gallery and view them later.
- View all artwork-gallery relationships
- Add  or remove the artwork-gallery mappings
  
**Unit Testing**: 
- Ensures that everything works well and implements "unittest" framework.
- Ensures the functionality of critical features

**Database Connectivity**: 
- Uses MySQL database, and the util package helps to connect securely.
- The Util package handles all the database connection operations cleanly
  
**Exception Handling**: 
- The system also has custom exceptions for meaningful reporting of errors.
- Handles edge cases like duplicate entries, invalid/missing IDs, etc.

**CLI - Based Interface**:
- Intuitive **Menu-driven Command-line Interface** for all user types
- Separate menu structures for Admins, Users, and Artists

**Tabular Displays**:
- Clean tabular display for all listings (artworks, artists, galleries, favorites) using the **tabulate**
- Enhances the readability in the cases of multiple outputs

**Soft-Delete Support**:
- Soft Deletion (Via deactivation) is supported for **users**, **artists**, and **galleries**

**Database Design Highlights**:
- Fully normalised relational schema using MySQL
- **Tables**:Artist, Artwork, Gallery, User, UserFavoriteArtwork, ArtworkGallery

**Strong database constraints**:
- Primary key, unique, and not null constraints for critical fields
- Foreign key for relationships
  - Artwork -> Artist (ON DELETE RESTRICT)
  - Gallery -> Artist (ON DELETE SET NULL)
  - UserFavoriteArtwork and ArtworkGallery both use a **composite primary key** and ON DELETE CASCADE for clean relational handling.

## Technologies Used:
- Python
- MySQL
- mysql.connector.python (DB Connection)
- Unittest (for testing)
- Pycharm (IDE)
- Tabulate (for giving clean table formats in terminal)

create database VirtualArtGallery;
use VirtualArtGallery;

-- Artist Table:
Create table Artist
(
Artist_ID int auto_increment primary key,
Name varchar(50) not null,
Biography text,
Birth_Date date,
Nationality varchar(50),
Website varchar(500),
Contact_Information varchar(255) unique,
IsActive boolean default true,
unique(Name, Birth_Date)
) auto_increment = 101;

-- Artwork Table:
Create table Artwork 
(
Artwork_ID int auto_increment primary key,
Title varchar(255) not null,
Description text,
Creation_Date date not null,
Medium varchar(255) not null,
Image_URL varchar(500),
Artist_ID int not null,
unique (Title, Artist_ID),
Foreign key (Artist_ID) references Artist(Artist_ID) on delete restrict
) auto_increment = 201;


-- Gallery Table:
Create table Gallery
(
Gallery_ID int auto_increment primary key,
Gallery_Name varchar(100) not null,
Gallery_Description text,
Gallery_Location varchar(255),
Curator_ID int,
Opening_Hours varchar(150),
Is_Active boolean default true,

unique (Gallery_Name, Gallery_Location),

Foreign key (Curator_ID) references Artist(Artist_ID) on delete set null,
index gallery_name_idx (Gallery_Name),
index curator_idx (Curator_ID)
) auto_increment = 301;

-- Users Table:
Create table Users
(
User_ID int auto_increment primary key,
User_Name varchar(50) not null unique,
User_Password  varchar(255) not null,
Email varchar(255) unique not null,
First_Name varchar(50) not null,
Last_Name varchar(50),
Date_Of_Birth date,
Profile_Picture varchar(500) default null,
Is_Active boolean default true 
) auto_increment = 401;
alter table Users add Role varchar(10) default 'user';

-- User_Favorite_Artwork Table:
Create table UserFavoriteArtwork 
(
User_ID int,
Artwork_ID int,
Primary key(User_ID, Artwork_ID),
Foreign Key (User_ID) references Users(User_ID) on delete cascade,
Foreign Key (Artwork_ID) references Artwork(Artwork_ID) on delete cascade
);

-- Artwork_Gallery table:
Create table ArtworkGallery
(
Artwork_ID int,
Gallery_ID int,
Primary key(Artwork_ID, Gallery_ID),
Foreign Key (Artwork_ID) references Artwork(Artwork_ID) on delete cascade,
Foreign Key (Gallery_ID) references Gallery(Gallery_ID) on delete restrict
);





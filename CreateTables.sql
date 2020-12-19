
create database ArtGallery;


show databases ;


use ArtGallery;


create Table Artist (Artist_ID INT PRIMARY KEY AUTO_INCREMENT,
                     First_Name CHAR(15),
                     Last_Name CHAR(20),
                     Phone VARCHAR(12),
                     Slug VARCHAR(100)
                     );

create Table Artist_Address (ID INT PRIMARY KEY AUTO_INCREMENT,
                             Home VARCHAR(255),
                             Office VARCHAR(255),
                             Slug VARCHAR(100),
                             Artist_ID INT,
                             FOREIGN KEY (Artist_ID) REFERENCES Artist(Artist_ID)
                                 ON DELETE CASCADE
                        );



create Table  Exhibition ( Exhibition_ID INT PRIMARY KEY AUTO_INCREMENT,
                          Start_Date DATETIME,
                          Exhibition_Name VARCHAR(100),
                          End_DATE DATETIME,
                          Venue VARCHAR(100),
                          Slug VARCHAR (100)
                                );


create Table Painting ( Painting_ID INT PRIMARY KEY AUTO_INCREMENT,
                        Painting VARCHAR(100),
			Painting_Name VARCHAR (59),
                        Year VARCHAR (4),
                        Sold BOOLEAN DEFAULT FALSE,
                        Slug VARCHAR (100),
                        Artist_ID INT,
                        FOREIGN KEY (Artist_ID) REFERENCES Artist(Artist_ID)
                            ON DELETE CASCADE
                      );


create Table Customer(Customer_ID INT PRIMARY KEY AUTO_INCREMENT,
                        First_Name CHAR(15),
                        Last_Name Char(20),
                        Address VARCHAR(100),
                        Phone INT(10),
                        Slug VARCHAR (100)
                     );





create Table auth_user (username VARCHAR(150) UNIQUE PRIMARY KEY NOT NULL,
                    	First_Name CHAR(150),
                     	Last_Name CHAR(150),
                    	Email VARCHAR(254) UNIQUE NOT NULL,
                    	Password VARCHAR(20) NOT NULL,
                    	Last_Login DATEIME(6) DEFAULT NULL,
                    	Is_Superuser BOOLEAN DEFAULT FALSE,
                     	Is_Staff BOOLEAN DEFAULT FALSE,
                     	Is_Active BOOLEAN DEFAULT FALSE,
			Date_Joined DATEIME(6) DEFAULT NULL            	
                    );


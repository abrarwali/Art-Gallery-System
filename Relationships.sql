

create Table Buy (
                         Price INT NOT NULL,
                         Painting_ID INT,
                         Currency VARCHAR(20),
                         Sold_In INT,
                         Artist_ID INT,
                         Customer_ID INT,
                         Slug VARCHAR(100)
                         FOREIGN KEY (Artist_ID) REFERENCES Artist(Artist_ID),
                         FOREIGN KEY (Painting_ID) REFERENCES Painting(Painting_ID),
                         FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID),
                         FOREIGN KEY (Sold_In) REFERENCES Customer(Exhibition_ID)
                       );


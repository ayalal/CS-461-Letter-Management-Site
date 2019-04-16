DROP TABLE IF EXISTS MonthlyInfo;
DROP TABLE IF EXISTS BottleSizes;
DROP TABLE IF EXISTS Dates;
DROP TABLE IF EXISTS Sizes;
DROP TABLE IF EXISTS Spirits;
DROP TABLE IF EXISTS Types;
DROP TABLE IF EXISTS Months;

CREATE TABLE Types(
	ID int NOT NULL AUTO_INCREMENT,
	Name varchar(255) NOT NULL,
	PRIMARY KEY (ID)
) ENGINE=InnoDB;

CREATE TABLE Spirits(
	ID int(11) NOT NULL,
	TypeID int NOT NULL,
	Description varchar(255) NOT NULL,
	Proof int (11) NOT NULL,
	PRIMARY KEY (ID),
	FOREIGN KEY (TypeID) REFERENCES Types(ID)
) ENGINE=InnoDB;

CREATE TABLE Sizes(
	ID varchar(255) NOT NULL,
	Val varchar(255) NOT NULL,
	PRIMARY KEY (ID)
) ENGINE=InnoDB;


CREATE TABLE BottleSizes(
	SpiritID int NOT NULL,
	SizeID varchar(255) NOT NULL,
	PRIMARY KEY (SpiritID,SizeID),
	FOREIGN KEY (SpiritID) REFERENCES Spirits(ID),
	FOREIGN KEY (SizeID) REFERENCES Sizes(ID)
) ENGINE=InnoDB;


Create TABLE Months(
	ID int NOT NULL AUTO_INCREMENT,
	Name varchar(255) NOT NULL,
	PRIMARY KEY (ID)
) ENGINE=InnoDB;

Create TABLE Dates(
	ID int NOT NULL AUTO_INCREMENT,
	Month int NOT NULL,
	Year year NOT NULL,
	PRIMARY KEY (ID),
	FOREIGN KEY (Month) REFERENCES Months(ID)
) ENGINE=InnoDB;	

CREATE TABLE MonthlyInfo(
	ID int NOT NULL AUTO_INCREMENT,
	MonthYear int NOT NULL,
	SpiritID int NOT NULL,
	SizeID varchar(255) NOT NULL,
	UnitPrice DECIMAL(13, 2) NOT NULL,
	PricePerCase DECIMAL(13, 2) NOT NULL,
	PricePerOz DECIMAL(13, 2) NOT NULL,
	PRIMARY KEY (ID),
	FOREIGN KEY (MonthYear) REFERENCES Dates(ID),
	FOREIGN KEY (SpiritID) REFERENCES Spirits(ID),
	FOREIGN KEY (SizeID) REFERENCES Sizes(ID)
) ENGINE=InnoDB;


/* testing data */
/* Add data to Types table */
INSERT INTO Types (Name) values ("Vodka");

/* Add data to Spirits table */
INSERT INTO Spirits (ID,TypeID,Description,Proof) values (8488,(SELECT ID FROM Types Where Name = "Vodka"),"TITO'S HANDMADE VODKA",80);
INSERT INTO Spirits (ID,TypeID,Description,Proof) values (0679,(SELECT ID FROM Types Where Name = "Vodka"),"SMIRNOFF VODKA 80",80);

/* Add data to Sizes table */
INSERT INTO Sizes (ID,Val) values ("A","LITER");
INSERT INTO Sizes (ID,Val) values ("B","750 ML");
INSERT INTO Sizes (ID,Val) values ("D","200 ML");
INSERT INTO Sizes (ID,Val) values ("E","375 ML");
INSERT INTO Sizes (ID,Val) values ("F","50 ML");
INSERT INTO Sizes (ID,Val) values ("H","1.75 L");

/* Add data to BottleSizes table */
INSERT INTO BottleSizes (SpiritID,SizeID) values ((SELECT ID FROM Spirits Where Description = "TITO'S HANDMADE VODKA"),(SELECT ID FROM Sizes Where ID = "D"));
INSERT INTO BottleSizes (SpiritID,SizeID) values ((SELECT ID FROM Spirits Where Description = "TITO'S HANDMADE VODKA"),(SELECT ID FROM Sizes Where ID = "E"));
INSERT INTO BottleSizes (SpiritID,SizeID) values ((SELECT ID FROM Spirits Where Description = "TITO'S HANDMADE VODKA"),(SELECT ID FROM Sizes Where ID = "F"));
INSERT INTO BottleSizes (SpiritID,SizeID) values ((SELECT ID FROM Spirits Where Description = "TITO'S HANDMADE VODKA"),(SELECT ID FROM Sizes Where ID = "H"));
INSERT INTO BottleSizes (SpiritID,SizeID) values ((SELECT ID FROM Spirits Where Description = "TITO'S HANDMADE VODKA"),(SELECT ID FROM Sizes Where ID = "B"));
INSERT INTO BottleSizes (SpiritID,SizeID) values ((SELECT ID FROM Spirits Where Description = "SMIRNOFF VODKA 80"),(SELECT ID FROM Sizes Where ID = "B"));
INSERT INTO BottleSizes (SpiritID,SizeID) values ((SELECT ID FROM Spirits Where Description = "SMIRNOFF VODKA 80"),(SELECT ID FROM Sizes Where ID = "D"));
INSERT INTO BottleSizes (SpiritID,SizeID) values ((SELECT ID FROM Spirits Where Description = "SMIRNOFF VODKA 80"),(SELECT ID FROM Sizes Where ID = "E"));
INSERT INTO BottleSizes (SpiritID,SizeID) values ((SELECT ID FROM Spirits Where Description = "SMIRNOFF VODKA 80"),(SELECT ID FROM Sizes Where ID = "F"));
INSERT INTO BottleSizes (SpiritID,SizeID) values ((SELECT ID FROM Spirits Where Description = "SMIRNOFF VODKA 80"),(SELECT ID FROM Sizes Where ID = "H"));

/* Add data to Months table */
INSERT INTO Months (Name) values ("January");
INSERT INTO Months (Name) values ("February");

/* Add data to Dates table */
INSERT INTO Dates (Month,Year) values ((SELECT ID FROM Months where Name = "January"),2019);
INSERT INTO Dates (Month,Year) values ((SELECT ID FROM Months where Name = "February"),2019);

/* Add data to MonthlyInfo table */
INSERT INTO MonthlyInfo (MonthYear,SpiritID,SizeID,UnitPrice,PricePerCase,PricePerOz) values ((SELECT ID FROM Dates WHERE Month = 1 and Year = 2019),(SELECT ID FROM Spirits WHERE Description = "TITO'S HANDMADE VODKA"),(SELECT ID FROM Sizes WHERE Val = "200 ML"),5.95,142.80,0.87);
INSERT INTO MonthlyInfo (MonthYear,SpiritID,SizeID,UnitPrice,PricePerCase,PricePerOz) values ((SELECT ID FROM Dates WHERE Month = 1 and Year = 2019),(SELECT ID FROM Spirits WHERE Description = "TITO'S HANDMADE VODKA"),(SELECT ID FROM Sizes WHERE Val = "375 ML"),11.95,143.40,0.94);
INSERT INTO MonthlyInfo (MonthYear,SpiritID,SizeID,UnitPrice,PricePerCase,PricePerOz) values ((SELECT ID FROM Dates WHERE Month = 1 and Year = 2019),(SELECT ID FROM Spirits WHERE Description = "TITO'S HANDMADE VODKA"),(SELECT ID FROM Sizes WHERE Val = "50 ML"),2.50,150.00,1.47);
INSERT INTO MonthlyInfo (MonthYear,SpiritID,SizeID,UnitPrice,PricePerCase,PricePerOz) values ((SELECT ID FROM Dates WHERE Month = 1 and Year = 2019),(SELECT ID FROM Spirits WHERE Description = "TITO'S HANDMADE VODKA"),(SELECT ID FROM Sizes WHERE Val = "1.75 L"),39.95,239.70,0.67);
INSERT INTO MonthlyInfo (MonthYear,SpiritID,SizeID,UnitPrice,PricePerCase,PricePerOz) values ((SELECT ID FROM Dates WHERE Month = 1 and Year = 2019),(SELECT ID FROM Spirits WHERE Description = "TITO'S HANDMADE VODKA"),(SELECT ID FROM Sizes WHERE Val = "750 ML"),23.95,287.40,0.94);
INSERT INTO MonthlyInfo (MonthYear,SpiritID,SizeID,UnitPrice,PricePerCase,PricePerOz) values ((SELECT ID FROM Dates WHERE Month = 1 and Year = 2019),(SELECT ID FROM Spirits WHERE Description = "SMIRNOFF VODKA 80"),(SELECT ID FROM Sizes WHERE Val = "750 ML"),12.95,155.40,0.50);
INSERT INTO MonthlyInfo (MonthYear,SpiritID,SizeID,UnitPrice,PricePerCase,PricePerOz) values ((SELECT ID FROM Dates WHERE Month = 1 and Year = 2019),(SELECT ID FROM Spirits WHERE Description = "SMIRNOFF VODKA 80"),(SELECT ID FROM Sizes WHERE Val = "200 ML"),4.95,237.60,0.72);
INSERT INTO MonthlyInfo (MonthYear,SpiritID,SizeID,UnitPrice,PricePerCase,PricePerOz) values ((SELECT ID FROM Dates WHERE Month = 1 and Year = 2019),(SELECT ID FROM Spirits WHERE Description = "SMIRNOFF VODKA 80"),(SELECT ID FROM Sizes WHERE Val = "375 ML"),8.95,214.80,0.70);
INSERT INTO MonthlyInfo (MonthYear,SpiritID,SizeID,UnitPrice,PricePerCase,PricePerOz) values ((SELECT ID FROM Dates WHERE Month = 1 and Year = 2019),(SELECT ID FROM Spirits WHERE Description = "SMIRNOFF VODKA 80"),(SELECT ID FROM Sizes WHERE Val = "50 ML"),1.75,210.00,1.02);
INSERT INTO MonthlyInfo (MonthYear,SpiritID,SizeID,UnitPrice,PricePerCase,PricePerOz) values ((SELECT ID FROM Dates WHERE Month = 1 and Year = 2019),(SELECT ID FROM Spirits WHERE Description = "SMIRNOFF VODKA 80"),(SELECT ID FROM Sizes WHERE Val = "1.75 L"),15.00,90.00,0.25);


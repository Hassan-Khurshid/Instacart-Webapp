CREATE TABLE ORDER
(
  Order_ID INT NOT NULL,
  Order_DOW INT NOT NULL,
  Order_Number INT NOT NULL,
  Days_Since_Prior_Order INT NOT NULL,
  User_ID INT NOT NULL,
  Order_Hour_of_Day INT NOT NULL,
  PRIMARY KEY (Order_ID)
);

CREATE TABLE ORDER_PRODUCTS
(
  Add-to-Cart_Order INT NOT NULL,
  Reordered INT NOT NULL,
  Order_ID INT NOT NULL,
  Product_ID INT NOT NULL,
  PRIMARY KEY (Order_ID),
  UNIQUE (Product_ID)
);

CREATE TABLE DEPARTMENT
(
  Department_ID INT NOT NULL,
  Department_Name INT NOT NULL,
  PRIMARY KEY (Department_ID)
);

CREATE TABLE AISLE
(
  Aisle_ID INT NOT NULL,
  Aisle_Name INT NOT NULL,
  PRIMARY KEY (Aisle_ID)
);

CREATE TABLE is_in;_has
(
  Order_ID INT NOT NULL,
  Order_ID INT NOT NULL,
  PRIMARY KEY (Order_ID, Order_ID),
  FOREIGN KEY (Order_ID) REFERENCES ORDER(Order_ID),
  FOREIGN KEY (Order_ID) REFERENCES ORDER_PRODUCTS(Order_ID)
);

CREATE TABLE PRODUCT
(
  Product_ID INT NOT NULL,
  Product_Name INT NOT NULL,
  Aisle_ID INT NOT NULL,
  Dept._ID INT NOT NULL,
  Department_ID INT NOT NULL,
  Aisle_ID INT NOT NULL,
  PRIMARY KEY (Product_ID),
  FOREIGN KEY (Department_ID) REFERENCES DEPARTMENT(Department_ID),
  FOREIGN KEY (Aisle_ID) REFERENCES AISLE(Aisle_ID)
);

CREATE TABLE has;_is_in
(
  Product_ID INT NOT NULL,
  Order_ID INT NOT NULL,
  PRIMARY KEY (Product_ID, Order_ID),
  FOREIGN KEY (Product_ID) REFERENCES PRODUCT(Product_ID),
  FOREIGN KEY (Order_ID) REFERENCES ORDER_PRODUCTS(Order_ID)
);
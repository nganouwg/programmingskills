

/*
    SELECT - extracts data from a database
    UPDATE - updates data in a database
    DELETE - deletes data from a database
    INSERT INTO - inserts new data into a database
    CREATE DATABASE - creates a new database
    ALTER DATABASE - modifies a database
    CREATE TABLE - creates a new table
    ALTER TABLE - modifies a table
    DROP TABLE - deletes a table
    CREATE INDEX - creates an index (search key)
    DROP INDEX - deletes an index
*/

-- Select all rows and columns
SELECT * from tbl1

-- Select speicific columns
SELECT Store, Item, department, subdepatment, category, subcategory from tbl1

-- Select distinct records from a table
SELECT DISTINCT Store, Item from tbl1

-- Order records by age ascending and height descending
SELECT * FROM tbl1 ORDER BY age ASC, height DESC 

-- Filter customers that are active 
SELECT * FROM tbl1 WHERE IsActive = TRUE

-- "AND": select customers that are active and located in Little Rock, AR
SELECT * FROM tbl1 WHERE IsActive = TRUE AND Country = 'USA' AND [State] = 'AR' AND City = 'Little Rock'

-- "OR" select customers that are active and located in Little Rock, AR or Houston, TX
SELECT * FROM tbl1 WHERE IsActive = TRUE AND Country = 'USA' AND 
                        (
                            ([State] = 'AR' AND City = 'Little Rock')
                            or 
                            ([State] = 'TX' AND City = 'Houston')
                        )

-- "NOT" select all customers that are active in Arkansas except Little Rock
SELECT * FROM tbl1 WHERE IsActive = TRUE AND Country = 'USA' AND [State] = 'AR' AND NOT City = 'Little Rock'

-- Count the total number of records
SELECT COUNT(*) from tbl1

-- Count Distint states 
SELECT COUNT(DISTINCT [State]) from tbl1 

-- Calculate the average salary by depatment
SELECT department, AVG(salary) from employee GROUP BY department

-- Null and Not Null 
SELECT * from tbl1 WHERE Zipcode IS NULL
SELECT * from tbl1 WHERE Zipcode IS NOT NULL

-- Select the TOP 5 oldest customer 
SELECT TOP 5 * from tbl1 ORDER BY Age DESC

-- Lowest and Highest prices
SELECT MIN(Price) AS lowest_price, MAX(Price) as highest_price FROM Products

-- Lowest price for each category
SELECT MIN(Price) AS lowest_price, category FROM Products group by Category

-- SUM up the total quantity of product sold for each order
SELECT OrderID, SUM(Quantity) AS [Total Quantity] FROM OrderDetails GROUP BY OrderID

-- Get the average prices of products by category
SELECT AVG(Price) AS AveragePrice, CategoryID FROM Products GROUP BY CategoryID

-- Like / Wildcards
/*

Symbol	Description
 %	    Represents zero or more characters
 _	    Represents a single character
 []	    Represents any single character within the brackets *
 ^	    Represents any character not in the brackets *
 -	    Represents any single character within the specified range *
 {}	    Represents any escaped character **
*/

SELECT * FROM Customers WHERE CustomerName LIKE '%es'

-- Return all customers with a City starting with "L", followed by any 3 characters, ending with "on":
SELECT * FROM Customers WHERE City LIKE 'L___on';

-- Return all customers starting with either "b", "s", or "p":
SELECT * FROM Customers WHERE CustomerName LIKE '[bsp]%';

-- Return all customers starting with "a", "b", "c", "d", "e" or "f":
SELECT * FROM Customers WHERE CustomerName LIKE '[a-f]%';

--Return all customers that starts with "a" and are at least 3 characters in length:
SELECT * FROM Customers WHERE CustomerName LIKE 'a__%';

-- Return all customers from 'Germany', 'France', or 'UK'
SELECT * FROM Customers WHERE Country IN ('Germany', 'France', 'UK');

-- Return all customers that are NOT from 'Germany', 'France', or 'UK':
SELECT * FROM Customers WHERE Country NOT IN ('Germany', 'France', 'UK');

-- Selects all products with a price between 10 and 20:
SELECT * FROM Products WHERE Price BETWEEN 10 AND 20;

-- Selects all products with a price not between 10 and 20:
SELECT * FROM Products WHERE Price NOT BETWEEN 10 AND 20;

-- The following SQL statement selects all products with a ProductName alphabetically between Carnarvon Tigers and Mozzarella di Giovanni:
SELECT * FROM Products WHERE ProductName BETWEEN 'Carnarvon Tigers' AND 'Mozzarella di Giovanni' ORDER BY ProductName;

-- We will join the Products table with the Categories table, by using the CategoryID field from both tables:
SELECT ProductID, ProductName, CategoryName FROM Products INNER JOIN Categories ON Products.CategoryID = Categories.CategoryID;

-- The following SQL statement will select all customers, and any orders they might have
SELECT Customers.CustomerName, Orders.OrderID FROM Customers LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID ORDER BY Customers.CustomerName;

-- The following SQL statement will return all employees, and any orders they might have placed:
SELECT Orders.OrderID, Employees.LastName, Employees.FirstName FROM Orders RIGHT JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID ORDER BY Orders.OrderID;

-- The following SQL statement selects all customers, and all orders:
SELECT Customers.CustomerName, Orders.OrderID FROM Customers FULL OUTER JOIN Orders ON Customers.CustomerID=Orders.CustomerID ORDER BY Customers.CustomerName;

-- The following SQL statement matches customers that are from the same city:
SELECT A.CustomerName AS CustomerName1, B.CustomerName AS CustomerName2, A.City FROM Customers A, Customers B WHERE A.CustomerID <> B.CustomerID AND A.City = B.City ORDER BY A.City;

-- The following SQL statement returns the cities (only distinct values) from both the "Customers" and the "Suppliers" table:
SELECT City FROM Customers
UNION
SELECT City FROM Suppliers
ORDER BY City;

-- The following SQL statement returns the cities (duplicate values also) from both the "Customers" and the "Suppliers" table:
SELECT City FROM Customers
UNION ALL
SELECT City FROM Suppliers
ORDER BY City;

-- The following SQL statement lists the number of customers in each country, sorted high to low (Only include countries with more than 5 customers):
SELECT COUNT(CustomerID), Country FROM Customers GROUP BY Country HAVING COUNT(CustomerID) > 5 ORDER BY COUNT(CustomerID) DESC;

-- The following SQL statement returns TRUE and lists the suppliers with a product price less than 20:
SELECT SupplierName FROM Suppliers WHERE EXISTS (SELECT ProductName FROM Products WHERE Products.SupplierID = Suppliers.supplierID AND Price < 20);

-- The following SQL statement lists the ProductName if it finds ANY records in the OrderDetails table has Quantity equal to 10 (this will return TRUE because the Quantity column has some values of 10):
SELECT ProductName FROM Products WHERE ProductID = ANY(SELECT ProductID FROM OrderDetails WHERE Quantity > 99);

-- The following SQL statement lists the ProductName if ALL the records in the OrderDetails table has Quantity equal to 10. This will of course return FALSE because the Quantity column has many different values (not only the value of 10):
SELECT ProductName FROM Products WHERE ProductID = ALL(SELECT ProductID FROM OrderDetails WHERE Quantity = 10);

-- The following SQL statement creates a backup copy of Customers:
SELECT * INTO CustomersBackup2017 FROM Customers;

-- The following SQL goes through conditions and returns a value when the first condition is met:
SELECT OrderID, Quantity,
CASE
    WHEN Quantity > 30 THEN 'The quantity is greater than 30'
    WHEN Quantity = 30 THEN 'The quantity is 30'
    ELSE 'The quantity is under 30'
END AS QuantityText
FROM OrderDetails;

-- The following SQL will order the customers by City. However, if City is NULL, then order by Country:
SELECT CustomerName, City, Country
FROM Customers
ORDER BY
(CASE
    WHEN City IS NULL THEN Country
    ELSE City
END);

-- Copy "Suppliers" into "Customers" (fill all columns):
INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
SELECT SupplierName, ContactName, Address, City, PostalCode, Country FROM Suppliers;

-- Insert a new customers into the customer table
INSERT INTO Customer_tbl (customerName, DateOfBirth, City, [State], Zipcode, Country)
VALUES ('John Doe', '01/01/1988', 'Little Rock', 'AR', '72202', 'USA'),
        ('Jane Doe', '01/01/1989', 'Houton', 'TX', '77001', 'USA')

-- Update the active status to false, and zipcode to null
UPDATE tbl1 SET IsActive = FALSE, Zipcode = NULL WHERE CustomerID = 21

-- Delete customer with no names
DELETE FROM tbl1 WHERE customerName is NULL OR CustomerName = ''




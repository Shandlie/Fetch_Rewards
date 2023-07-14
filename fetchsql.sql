CREATE SCHEMA fetch_rewards;

USE fetch_rewards;

CREATE TABLE Rewards(
	receipts_id         	INTEGER  NOT NULL PRIMARY KEY          
	,purchasedItemCount     NUMERIC(7,5) NOT NULL               
	,totalSpent          	NUMERIC(7,5) NOT NULL   
	,PointsEarned         	NUMERIC(7,5) NOT NULL  	
	,purchaseDate	      	NUMERIC(7,5) NOT NULL	
	);

CREATE TABLE Receipts(
	receipts_id         	INTEGER  NOT NULL PRIMARY KEY          
	,bonusPointsEarnedReason    	    VARCHAR(24) NOT NULL              
	,rewardsReceiptItemList          	VARCHAR(24) NOT NULL 
	,rewardsReceiptStatus         		VARCHAR(24) NOT NULL  	
	);
    
-- Question 2 --
-- When considering total number of items purchased from receipts with 'rewardsReceiptsStatus' of 'Accepted' or 'Rejected', which is greater? --

SELECT 
	CASE
		WHEN accepted.total-items_purchased > rejected.total_items_purchased THEN 'Accepted'
		WHEN accepted.total_items_purchased < rejected.total_items_purchased THEN 'Rejected'
		ELSE 'Equal'
	END AS greater
FROM
	(SELECT
		SUM(purchasedItemCount) AS total_items_purchased
FROM Rewards
JOIN Receipts ON Rewards.receipts_id = Receipts.receipts_id
WHERE 
	Receipts.rewardsReceiptsStauts = 'Accepted') AS accepted,
(SELECT SUM(purchasedItemCount) AS total_items_purchased
FROM Rewards
JOIN Receipts on Rewards.receipts_id = Receipts.receipts_id
WHERE Receipts.rewardsReceiptStatus = 'Rejected') 
AS Rejected;

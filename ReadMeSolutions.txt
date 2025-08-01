In the "python" folder you can find scripts that were created for processing the data.
The "solutions" folder contains the results of calculations as csv files. 

1. RevenueCalculator 
It takes json file with trades as an input, multiplies the quantity by the price and creates revenue for each trade. 
At the end it calculates the total revenue over all trades.

2. ImbalanceCalculator
This method calculates the difference between forecasted and measured production and multiplies this difference by the penalty rate. 
The results for each asset are stored as separate files (imbalance_mp1, imbalance_mp2 etc).

3. Invoicing
There are 4 methods here. The first method calculates the infeed payout: production * price. 
If price is fixed, we take it from the file with base data. If market price modeling is used, we take the index from market_index_prices.csv. 
The second methods does the similar but for fee: at this point the method only calculates fee for "fixed as produced" and "percent of market" 
fee models. Third and forth methods calculate VAT and total gross amount of the infeed payout. 

4. Report
This methods should summarize the data for all assets as a table. Now it only has data about infeed payout. 
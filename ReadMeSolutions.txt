In the "python" folder you can find scripts that were created for processing the data.
The "solutions" folder contains the results of calculations as csv files. 



1. RevenueCalculator 

It takes json file with trades as an input, multiplies the quantity by the price and calculates revenue for each trade. 
At the end it calculates the total revenue over all trades.



2. ImbalanceCalculator

This method calculates the difference between forecasted and measured production and multiplies this difference by the penalty rate. 
The difference is divided by 1000 to convert kw into mw.
The results for each asset are stored as separate files (imbalance_mp1, imbalance_mp2 etc).



3. Invoicing

There are 4 methods here. The first method calculates the infeed payout: measured production * price. Measured production 
is also converted in MW by dividing into 1000.
If price is fixed, we take it from the file with base data. If market price modeling is used, we take the index from market_index_prices.csv. 

The second methods calculates the fee: at this point the method only works for "fixed as produced" 
and "percent of market" fee models. 

fee (fixed as produced) = measured * fee__eur_per_mwh
fee (market percent) = measured * fee_percent * average market index

Third and forth methods calculate VAT and total gross amount of the infeed payout. 

4. Report
This method should summarize the data for all assets as a table. Now it only has data about infeed payout. 
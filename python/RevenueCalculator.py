import json
import pandas as pd

# Calculating revenue for each trade and also the total revenue
def calculate_revenue(trades_path):

    with open(trades_path) as file:
        trades = json.load(file)

    df_trades = pd.DataFrame(trades)
    df_trades["revenue"] = df_trades["price"] * df_trades["quantity"]
    total_revenue = df_trades["revenue"].sum()

    total_row_df = pd.DataFrame([total_revenue], index=['Total']) 

    df_total = pd.concat([df_trades, total_row_df])

    df_total.to_csv("solutions/trades_revenue.csv", sep=";", index=True)

# Applying the method
calculate_revenue("trades.json")


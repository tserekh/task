import random
import pandas as pd


def report(df_orders, df_lines, N=10):
    # средний чеки и суммарные продажи я считал за весь доступный переод, так как явно не указано

    df_orders_last = df_orders[(
        pd.Timestamp.now()-df_orders['DateTime']).apply(lambda x: x.days <= 30)]
    df_lines_gb = df_lines[df_lines['OrderID'].isin(
        df_orders_last['OrderID'])].groupby(['ProductID']).size()
    top_products = pd.DataFrame(df_lines_gb).sort_values(
        0, ascending=False).iloc[:N].index
    df_prod_total_sales = df_lines[df_lines['ProductID'].isin(
        top_products)].groupby('ProductID')['price'].sum()
    df_sum = pd.DataFrame(df_lines.groupby(['OrderID'])['price'].sum())
    df_sum.columns = ['sum']
    df_prod_mean_ticket = pd.merge(df_sum, df_lines[df_lines['ProductID'].isin(top_products)][[
                                   'OrderID', 'ProductID']], on='OrderID').groupby('ProductID')['sum'].mean()
    result = pd.DataFrame(df_prod_total_sales).join(df_prod_mean_ticket)
    result = result.rename(
        columns={'sum': 'mean_ticket', 'price': 'total_revenue'})
    return result

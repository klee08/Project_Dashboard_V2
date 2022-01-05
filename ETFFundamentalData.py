#STOCK FINANCIAL STAEMENT DDWNLOADER  V.1.0 - Latest Update 2022.01.07> 
#Download Financial Statement Data and store into Sql DB 
#Author: Ken Lee 

import yfinance as yf
import pandas as pd
from datetime import datetime
import sqlalchemy as sql
import ETFHistoryDownload as hist

# Database connection string
eft_data_connection_string = 'sqlite:///./Resources/etf.db'
# Database engine
etf_data_engine = sql.create_engine(eft_data_connection_string, echo=True)

eft_data_connection_string2 = 'sqlite:///./Resources/etf.db'
# Database engine
etf_data_engine2 = sql.create_engine(eft_data_connection_string, echo=True)


keys_financial = {
    'symbol':'Symbol',
    'sector':'Sector',
    'shortName':'Name',
    'mostRecentQuarter':'Date_MostRecentQuarter',
    'lastDividendDate':'Date_LastDividend',
    'lastFiscalYearEnd':'Date_LastFiscalYearEnd',
    'nextFiscalYearEnd':'Date_NextFiscalYearEnd',
    'beta':'Beta',
    'bookValue':'BookValue',
    'debtToEquity':'Debt_to_Equity',
    'dividendRate':'Divedend_Rate',
    'fiveYearAvgDividendYield':'Dividend_5yrAvg',
    'lastDividendValue':'Dividend_LastValue',
    'trailingAnnualDividendRate':'Dividend_Rate_TrailngAnnual',
    'trailingAnnualDividendYield':'Dividend_TrailingAnnual',
    'dividendYield':'Dividend_Yield',
    'earningsGrowth':'Earning_Growth',
    'earningsQuarterlyGrowth':'Earning_QuarterGrowth',
    'ebitda':'EBITDA',
    'enterpriseToEbitda':'Enterprise_EBITDA',
    'enterpriseToRevenue':'Enterprise_Revenue',
    'enterpriseValue':'Enterprise_Value',
    'trailingEps':'EPS_Trailing',
    'ebitdaMargins':'Margin_EBITDA',
    'grossMargins':'Margin_Gross',
    'operatingMargins':'Margin_Operation',
    'profitMargins':'Margin_Profit',
    'marketCap':'MarketCap',
    'longName':'Name_Long',
    'forwardPE':'PE_FWD',
    'trailingPE':'PE_Trailing',
    'pegRatio':'PEG_FWD',
    'trailingPegRatio':'PEG_Trailing',
    'priceToBook':'Price_to_Book',
    'priceToSalesTrailing12Months':'PS_12m',
    'twoHundredDayAverage':'PX_200dAvg',
    'fiftyTwoWeekHigh':'PX_2weeksHigh',
    'fiftyTwoWeekLow':'PX_2weeksLow',
    'morningStarOverallRating':'Rating_MorningStar',
    'recommendationMean':'Rating_RecommendMean',
    'currentRatio':'Ratio_Current',
    'payoutRatio':'Ratio_DivPayout',
    'shortRatio':'Ratio_Short',
    'returnOnAssets':'Return_on_Asset',
    'returnOnEquity':'Return_on_Equity',
    'revenuePerShare':'Revenue_per_share',
    'targetHighPrice':'TargetPX_High',
    'targetLowPrice':'TargetPX_low',
    'targetMeanPrice':'TargetPX_Mean',
    'targetMedianPrice':'TargetPX_Median',
    'totalCash':'Total_Cash',
    'totalCashPerShare':'Total_Cash_per_Share',
    'totalDebt':'Total_Debt',
    'totalRevenue':'Total_Revenue',
    'averageDailyVolume10Day':'Volume_10dAvg'}

symbols = ['FB', 'AMZN']

def drop_table(p_table_name):
    connection = etf_data_engine.raw_connection()
    cursor = connection.cursor()
    command = "DROP TABLE IF EXISTS {};".format(p_table_name)
    cursor.execute(command)
    connection.commit()
    cursor.close()

def create_df(p_symbols):
    l_column_names = list(keys_financial.values())
    l_df = pd.DataFrame(columns = l_column_names)
    l_df.set_index('Symbol')
    for stock in p_symbols:
        l_df = l_df.reindex(l_df.index.values.tolist()+[stock])
    return l_df


def create_df_by_df_symbol(p_symbols_df):
    l_column_names = list(keys_financial.values())
    l_df = pd.DataFrame(columns = l_column_names)
    
    l_name_df = p_symbols_df.copy()
    if 'symbol' in l_name_df:
        print('a')
        # do nothing
    elif 'name' in  l_name_df:
        l_name_df['symbol'] = l_name_df['name']
    elif 'Symbol' in l_name_df:
        l_name_df['symbol'] = l_name_df['index']
    elif 'Symbol' in l_name_df:
        l_name_df['symbol'] = l_name_df['Symbol']
    else:
        l_name_df['symbol'] = l_name_df.index
    
    l_df['Symbol'] = l_name_df['symbol'].values
    
    l_df.set_index('Symbol')
    
    return l_df

def download_finData(p_output_df, p_symbols):
    #display(output_df)
    for l_symbol in p_symbols:
        #print(stock)
        #if stock in output_df.index:
        #    print("do nothing")
        #else:
        #    output_df = output_df.reindex(df.index.values.tolist()+[stock])
        #    output_df = output_df.drop_duplicates(keep ='first')
        l_info = yf.Ticker(l_symbol).info
        for l_key in keys_financial :
            l_value = l_info.get(l_key)
            try:
                if 'Date_' in keys_financial [l_key]:
                    if l_value != 'None':
                        p_output_df.at[l_symbol,keys_financial [l_key]] = datetime.utcfromtimestamp(int(l_value)).strftime('%Y-%m-%d %H:%M:%S')
                else:
                    p_output_df.at[l_symbol,keys_financial [l_key]] = l_value
            except:
                p_output_df.at[l_symbol,keys_financial [l_key]] = l_value
                
            #print(f"{stock} - {key} -- {keys[key]}: {info.get(key)}")
    p_output_df.to_sql('FINANCIAL_DATA', etf_data_engine, index=True, if_exists='replace')
    return p_output_df

def download_finData_by_df_Symbol(p_output_df, p_symbols_df):
    #display(output_df)
 
    l_name_df = p_symbols_df.copy()
    if 'symbol' in l_name_df:
        print('a')
        # do nothing
    elif 'name' in  l_name_df:
        l_name_df['symbol'] = l_name_df['name']
    elif 'Symbol' in l_name_df:
        l_name_df['symbol'] = l_name_df['index']
    elif 'Symbol' in l_name_df:
        l_name_df['symbol'] = l_name_df['Symbol']
    else:
        l_name_df['symbol'] = l_name_df.index

    for l_symbol in l_name_df['symbol']:

        #print(stock)
        #if stock in output_df.index:
        #    print("do nothing")
        #else:
        #    output_df = output_df.reindex(df.index.values.tolist()+[stock])
        #    output_df = output_df.drop_duplicates(keep ='first')
        l_info = yf.Ticker(l_symbol).info
        for l_key in keys_financial :
            l_value = l_info.get(l_key)
            try:
                if 'Date_' in keys_financial [l_key]:
                    if l_value != 'None':
                        p_output_df.at[l_symbol,keys_financial [l_key]] = datetime.utcfromtimestamp(int(l_value)).strftime('%Y-%m-%d %H:%M:%S')
                else:
                    p_output_df.at[l_symbol,keys_financial [l_key]] = l_value
            except:
                p_output_df.at[l_symbol,keys_financial [l_key]] = l_value
                
            #print(f"{stock} - {key} -- {keys[key]}: {info.get(key)}")
    p_output_df.to_sql('FINANCIAL_DATA', etf_data_engine, index=True, if_exists='replace')
    return p_output_df



def get_finData(p_portfolio_df):

    l_name_df = p_portfolio_df.copy()
    if 'symbol' in l_name_df:
        print('a')
        # do nothing
    elif 'name' in  l_name_df:
        l_name_df['symbol'] = l_name_df['name']
    elif 'Symbol' in l_name_df:
        l_name_df['symbol'] = l_name_df['Symbol']
    else:
        l_name_df['symbol'] = l_name_df.index

    l_names = hist.get_where_condition(l_name_df, 'symbol')
    l_sql_query = f"""
    SELECT * FROM FINANCIAL_DATA WHERE Symbol in ({l_names})
    """
    l_finData_df = pd.read_sql_query(l_sql_query, eft_data_connection_string)
    return l_finData_df
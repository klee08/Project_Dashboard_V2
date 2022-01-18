ETF Dashboard V2 Incorporated for Machine Learning
- Team 7: Ken, Albert, William and Rabia
- Readme author - Rabia and Ken Lee 2022-01-16

I. Project overview
- Enhance stock screening process by adding both Technical (Performance) and Financial (Fundamental) Analysis by using both Using Alpaca and Yahoo Finance Data 
- Leverage two machine Learning models and Colab cloud for stock price prediction (LSTM Regression Analysis) and Algorithmic trading (Deep Convolutional Neural Networks with execution signal (buy/hold/sell)
- Add Portfolio and Performance management to create and revamp up our new Portfolio [WKRA] ($ 1,000,000 USD) 

Presentation(Complete Detail): https://docs.google.com/presentation/d/1h6kvGb_6y4TC3zCaCfaiNC9UBA9HESKRjNTkuy4BBRU/edit#slide=id.gc6f9e470d_0_0

II. Dashboard V2 - 4 Functinality Domains:
1. Technical Stock Screener analyzes individual historical performance such as moving averages with volume and Relative Strength(RS) Rating to selects allocation asset candidates based on our screening criteria
2. Financial Analyzer reviews financial statement data of selected allocation candidates and compare with sector average 
to determines allocation strategy and weight
3. AlgoTrader proactively manages our position in volatile market and executing trades our investment model and strategy 
to maximize the profit and reduce the risk
4. Performance Surveillance captures risk exposure in advance by proactive market forecast and monitoring and 
ML Model breakage thru back testing and also helps rebalancing/revamping assets every 6 month 

III. Detailed usage and Jupyter notebooks: 
1) ETF_v2_1_StockScreener.ipynb 

- screen the best performers by using criteria based on SMA 50/150/200/200_20/HIGH_52WK/LOW_52WK, RelativeStrength RS Rating w/ Multiple and SP 500 
- Inspired from Mark Minervini's Trend Template
- http://www.minervini.com/blog/index.php/blog/first_things_first_how_to_chart_stocks_correctly_and_increase_your_chances.

2) ETF_v2_2_FinancialAnalyzer.ipynb

Analyze Financial Profitability and Stability by using Piotroski F-score and Altman Z Scoring metrices 
Simplified F-Score and Z-Score due to data limitation (only latest quarterly reporting available from Yahoo Finance)

3-1) ETF_v2_3a_AlgoDataGenerator.ipynb

Calculate Relatvie Strength Index(RSI), Money Flow Index(MFI), Return on capital(ROC), 
CMO, SMA, EMA, WMA, HWA< IRIX, CCI, DPO KST to generate Fresh Rolling Train Data per stock name

3-2) ETF_v2_3b_AlgoTrader.ipynb

Algorithmic Financial Trading with Deep Convolutional Neural Networks
*inspired by paper "Algorithmic Financial Trading with Deep Convolutional Neural Networks: Time Series to Image Conversion Approach:
implemenetation reference for neural network prediction model: https://towardsdatascience.com/stock-market-action-prediction-with-convnet-8689238feae3
ML Training Process:
a. Normalization: used MinMaxScaler from Sklearn to normalize the dat
b. Group indicators in the image based on types such as mementum and oscillator and train many CNN architectures
c. Reshape tabular data with 225 features as image
![Image Reshape](https://github.com/klee08/Project_Dashboard_V2/blob/main/Resources/image1.PNG)
d. Calculate Sample weight and pass it to Keras fit to deal with class imbalance
e. Neural Network Training model: InputLayer --> Conv2D --> Dropout --> Conv2D --> MaxPooling2D --> Dropout --> Flatten --> Dense --> Dropout --> Dense
f. BackTesting and Validating thru F1 Score and kappa
![Model Loss](https://github.com/klee08/Project_Dashboard_V2/blob/main/Resources/image2.PNG)

4-1) ETF_V2_4a PortfolioPricePrediction.ipynb

Stock Price Prediction and Forecasting using Stacked LSTM
- Colab integration version also available at https://colab.research.google.com/drive/1VgtwjDL0uEKNQYNOMgJmVTk1mo1cTXC8?usp=sharing
- Supervised Regression
ML Training Process:
a. Used min-max scalar to transform the values from 0 to 1
b. Split Train and Test by 60%
c. Used Sequential Model aand added LSTM Layers to train the model
d. fit X_train and y_train 
e. back testing -Predicted Open vs. Actual open
![Back Test](https://github.com/klee08/Project_Dashboard_V2/blob/main/Resources/image3.PNG)
- Discuss any unanticipated insights or problems that arose and how you resolved them.
   Hard to improve accuracy and data loss - more research required to train better

4-2) ETF_v2_4b PortfolioPositionMgmt.ipynb

- Cumulative Return, Performance Comparison to SP500 and other benchmarks, Monte Carlo simulation  
- Position Management POC (Proof of Concept -- need to integrated with AlgoTrading)

IV. Installation instructions
installation instructions
!pip install dateutils
!pip install sqlalchemy
!pip install hvplot
!pip install --upgrade tensorflow
!pip install -U scikit-learn
!pip install matplotlib

growth and dividend methods. Linear regression model was used to be able to better forecast futures of our portfolio. Maximizing profits algorithmic trading was implemented to periodic rebalancing into our portfolio.

V. Data Source:
-------------------------
1. Alpaca  API (V1) -- Price History Close, Volume
2. US News -- ETF Ratings by sector and Underlying stock names 
3. Yahoo Finance -- Financial Statement, balance Sheet and Ratios
4. Fidelity and FinVisualization- Performance baseline by sector. (download as csv) 
--------------------------   
  
VI. Relevant code or demonstrations of the machine learning model.
   1. https://github.com/klee08/Project_Dashboard_V2
      - ETF_v2_3a_AlgoDataGenerator.ipynb
      - ETF_v2_4b PortfolioPositionMgmt.ipynb
   2. Google Colab Sample - URL: https://colab.research.google.com/drive/1VgtwjDL0uEKNQYNOMgJmVTk1mo1cTXC8?usp=sharing

VII. Futher Improvement Points:
  - Need to improve ML Accuracy and prevent loss further by doing more research
  - Automatic trade execution and position management 
  - Leverage Google Colab and AWS Cloud to make application more scalable and add more epoch and GPU for ML

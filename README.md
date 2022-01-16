# Project_Dashboard_V2
# Project Goal:

# Project Requirements: 
1) Two Techniques we will focus:
- Google Colab (Cloud)
- Scikit-learn (ML) or TensorFlow/Keras
2) Projects:
- Compare two or more machine-learning models for solving a predictive task.
- Use machine learning to build a sophisticated algorithmic trading bot.

# Presentation
This is what you need for your presentation:
- An executive summary of the project and project goals. (5 points)
Explain how this project relates to fintech and machine learning.
The selected model. (5 points)

Rebalancing the portfolio (short/long) with Machine learning
# V2 Enhancement:
+ ML1. Time Series - Linear Regression Study (supervised)
+ ML2. Cherry Picking new names to short/loang
+ ML3. Periodic Rebalancing (execution)

- Describe the machine learning model that your group selected and why.
The data preparation and model training process. (3 points)
1. Scikit-learn (ML) --- linear Regression for price movement
2. TensorFlow/Keras  --- ? 

- Describe the source of your data and why you chose it for your project.
-------------------------
1. Alpaca  API (V1) -- Price History Close, Volume
2. US News -- ETF Ratings by sector and Underlying stock names 
3. Yahoo Finance -- Financial Statement, balance Sheet and Ratios
--------------------------
4. Fidelity - Performance baseline by sector. (download as csv) 
   Step1: Review the example: Automated-Fundamental-Analysis/stockratings.py at d3a9145c529804e72593f79406b8d28b93da04c1 · faizancodes/Automated-Fundamental-Analysis
   Step2: Find the good website to provide the performance summary by Sector to make comparison 
   -- getOverallRating(valuationGrade, profitabilityGrade, growthGrade, perfGrade, volatility)
   e.g. profitabilityGrade
        profitabilityStats.append(['Net Margin', profitMargin])
        profitabilityStats.append(['Operating Margin', operMargin])
        profitabilityStats.append(['Gross Margin', grossMargin])
        profitabilityStats.append(['ROE', roe])
        profitabilityStats.append(['ROA', roa])
    Sector         PriceChange    Avg ROE, AVG ROA, Net Margin,    
    Technology:   
     https://eresearch.fidelity.com/eresearch/markets_sectors/sectors/sectors_in_market.jhtml  

- Describe the collection, cleanup, and preparation process.
  - Apply Grading on Fundamental Data by 5 segments and covert to numbers so that we can use them for X for training -- William 
  - Normalize the data as a part of Clean up process -- Ken  

- Describe the training process.
  - Hisorical Price Movement analysis -- Supervised linear Regression ML
  - Cherry Picking - Unsupervised ML  with sample X and Y 
  - Algo training - find Exit and Replacement points for porfolio rebalancing

- The approach that your group took to achieve the project goals. (5 points)
   1. Build 5 Functions to getOverallRating (see example and rewrite our own codes) -- William w/ Industrial baseline download #4
   2. Enhance Historical price analysis by leaveraging Supervised ML Linear Regression -- Albert
   3. Train the Model for Cherry picking of best performers (Unsupervised ML)  -- Ken 
   4. Build Algo Trading logic to reblance our portfolio periodic basis (Unsupervised ML) -- Albert
   5. Summerize the ourcome and our model v2 approaches -- Presentation -- Rabia (Convert this Readme to presentation DRAFT)
  
   
- Include any relevant code or demonstrations of the machine learning model.
   1. https://github.com/klee08/Project_Dashboard_V2
   2. Google Colab Jupyter lab - URL: ?? (will be added)

- Describe the techniques that you used to evaluate the performance of the model.
   1. Forecast: MonteCarlo + prediction/surveillance techniques 
   2. Look Back: and back pricing -- leveraging known history
   
- Discuss any unanticipated insights or problems that arose and how you resolved them.
   -- TO-DO LIST for v3 improvement 
   
- The results and conclusions from the machine learning model or application. (5 points)
   --- WILL BE ADDED

- Include relevant images or examples to support your work.
   --- WILL BE ADDED

- If the project goal wasn’t achieved, share the issues and what the group tried for resolving them.
- Next steps. (2 points)
Take a moment to discuss the potential next steps for the project.
Discuss any additional questions that you’d explore if you had more time. 
Specifically, if you had additional weeks to work on your project, what would you research next?
    --- WILL BE ADDED

Next Step



# Steps:
1. Enhanced Cherry picking logic -- Fundamental Analysis and Price Movement Regression 
2. Historical data analysis with ML supervised time seris
3. Algoritm Trading execution - rebalancing
4. Monitoring performance 

testing
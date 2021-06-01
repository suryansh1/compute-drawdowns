# compute-drawdowns

This is homework 1 of the course FRE 7811 - Intro to Quantitative Trading  at NYU Tandon School of Engineering, Spring 2021.


### What  is a drawdown

 As per [Investopedia](https://www.investopedia.com/terms/d/drawdown.asp),

A drawdown is a peak-to-trough decline during a specific period for an investment, trading account, or fund. A drawdown is usually quoted as the percentage between the peak and the subsequent trough. If a trading account has $10,000 in it, and the funds drop to $9,000 before moving back above $10,000, then the trading account witnessed a 10% drawdown

### What this program does

Given time series data of PnL for a given instrument in a CSV format, this program computes the number of drawdowns in the data.
It also computes the depth of each drawdown, and its corresponding recovery time

Each drawdown has the following attributes, which are defined in the drawdown class

        
        * openingTime, closingTime : corresponding to when the drawdown started and ended    
        
        * recoveryTime : which is the time duration for which the drawdown lasted.        
        
        * peak : which corresponds to the maximum depth of a given drawdown
        
        
        
For a PnL time series, the for loop interates through the daily pnl values and computes how much, as a percentage of the _maximum-pnl-value-until-today_, is the difference between the current day's pnl value and the _maximum-pnl-value-until-today_. This percentage value for each day is stored in the list `drawdownValues`


Then, it decides whether 

 * a new drawdown is beginning  - Happens if the drawdownValues rise from zero to a non zero value
    * If so, initializes a new object of the drawdown class and sets the _openingTime_   
 * the current drawdown is still ongoing, happens if _drawdownValues_ have not reached zero after drawdown began
    * Simply computes the current drawdown's peak, by comparing today's _drawdownValue_ with the peak until today
 * the current drawdown is coming to a close - Happens if drawdownValues reach zero from a non zero value
    * If so, assign the _peak_, _closingTime_ and _recoveryTime_ for the closing drawdown


At the end it plots all the _drawdownValues_ using matplotlib and lists out all drawdowns.

Note : The class _CSVfile_ is a simple wrapper to read the relevant column from a given csv file

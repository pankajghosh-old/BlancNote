title: VaR - Value at Risk
date: 2014-04-12
tags: [Finance, Valuation]

#### An approximate measure of portfolio's potential risk

*This post is a work-in-progress*

### What is VaR?
For a given confidence level and a given time horizon, VaR is your portfolio's maximum likelihood loss. 

Let's say a portfolio has 1 week 95% VaR of $100 million. This means there is 5% chance that my portfolio can lose value of more than $100 million within 1 week.


### How is VaR calculated?

We begin with a set of assumptions: 

 + A portfolio consisting of a stock S, of quantity \\( \Delta \\) stock
 + A time horizon \\( {dt} \\)
 + Stock returns follow Normal distribution with volatility \\( \sigma \\) and drift \\( \mu \\)

... and try to estimate 99% VaR of this portfolio.
 
For short periods of \\( {dt} \\), we can ignore impact of drift on movement of stock price.
Standard deviation of stock price over this time horizon would be $$ \sigma S \sqrt{dt} $$
Standard deviation of portfolio would then be $$ \Delta \sigma S \sqrt{dt} $$

![Alt text](http://upload.wikimedia.org/wikipedia/commons/2/25/The_Normal_Distribution.svg)

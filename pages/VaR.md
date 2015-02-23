title: VaR - Value at Risk
date: 2014-04-12
tags: [Finance, Valuation]

#### An fractile measure of portfolio's risk

*This post is a work-in-progress*

### What is VaR?
For a given confidence level, $\alpha$ and a given time horizon, T, VaR is your portfolio's minimum likelihood loss with probability $1-\alpha$ over that time horizon. This is equivalent to saying that VaR is maximum likelihood loss of the portfolio at confidence level $\alpha$ over a period T.

By saying a portfolio has 1 week 95% VaR of \$100 million, we mean

 + There is 5% chance that the portfolio can lose value of atleast \$100 million within 1 week. 
 + We are 95% confident that portfolio will not lose more than \$100 million within 1 week.

VaR does *not* explicitly state how great losses could be in $\1-alpha$ cases. 
We will look at another measure, CVaR, which answers this question later.

### How is VaR calculated?

We begin with a set of assumptions: 

 + A portfolio consisting of a stock S, of quantity \\( \Delta \\) stock
 + Stock returns follow Normal distribution with volatility \\( \sigma \\) and drift \\( \mu \\)

Let's try to calculate 99% VaR of this portfolio.

	VaR = $V$
 
For short periods of \\( {dt} \\), we can ignore impact of drift on movement of stock price.
Standard deviation of stock price over this time horizon would be $$ \sigma S \sqrt{dt} $$
Standard deviation of portfolio would then be $$ \Delta \sigma S \sqrt{dt} $$

Assuming a stock's returns follow gaussian distribution, VaR of this portfolio, commonly known as Parametric VaR, is linearly proportional to its volatility. Higher the volatility of stock, higher its VaR, that sounds intuitive.




![Alt text](http://upload.wikimedia.org/wikipedia/commons/2/25/The_Normal_Distribution.svg)

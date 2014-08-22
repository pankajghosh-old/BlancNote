title: Why lognormal returns?
date: 2014-07-21
tags: [Finance, Valuation]

#### An exploration into why do we model stock returns by lognormal distribution?

*This post is a work-in-progress*

####What is normal distribution?
Also known as "Gaussian" distribution, Normal distribution refers to a family of symmetric continuous distributions characterized by a bell shaped curve around mean \\( \mu \\). Two parameters: mean \\(\mu\\) and variance \\(\sigma^2\\) are enough to define the shape of distribution. 
<!---
Any normal random variable, X ~ N(\\(\mu,\sigma^2)\\), would have a probability distribution function is $$ \frac {1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$
-->

####What is lognormal distribution?
Lognormal distribution is a continuous distribution in which logarithm of the random variable is normally distributed. If *Z* is a standard normal variable, $$ X = e^{\mu + \sigma Z}$$, X is log-normally distributed with mean \\( e^{\mu+\sigma^2/2} \\) and variance \\( (e^{\sigma^2} - 1)e^{2\mu+\sigma^2}\\)

####Relationship between normal and lognormal distribution

####Modeling stock returns
* Returns can be modeled as independant random variables
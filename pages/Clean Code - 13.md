title: Dependency Inversion Principle
date: 2014-04-18
tags: [CleanCode]

#### Decoupling high-level use-cases/policy modules and low-level/implementation-detail modules through abstractions.

Watch the original episode [here][1]

Let's start with an example, shall we?  
We are building a social application, Sociale (Ha!), which posts statuses to all of user's connected social networks.
We would like to decouple for two reasons

* Depending on how many social networks user has connection our application to  
* Test 123

<!--

[Sociale]->[Twitter|+PostStatus()]

-->

![](http://yuml.me/diagram/plain;/class/[Sociale]-%3E[Twitter%7C+PostStatus(\)])


<!--

[Sociale]putchar() -.-> [<<IO Driver>>;putchar()]
[<<IO Driver>>;putchar()]^-.-[Facebook],[<<IO Driver>>;putchar()]^-.-[Twitter],[<<IO Driver>>;putchar()]^-.-[FourSquare]

-->
![](http://yuml.me/diagram/plain;/class/[Sociale]PostStatus(\)%20-.-%3E%20[%3C%3CIO%20Driver%3E%3E;PostStatus(\)],%20[%3C%3CIO%20Driver%3E%3E;PostStatus(\)]%5E-.-[Facebook],[%3C%3CIO%20Driver%3E%3E;PostStatus(\)]%5E-.-[Twitter],[%3C%3CIO%20Driver%3E%3E;PostStatus(\)]%5E-.-[FourSquare])


[1]: http://cleancoders.com/episode/clean-code-episode-13/show
[2]: http://www.teradatatips.com/
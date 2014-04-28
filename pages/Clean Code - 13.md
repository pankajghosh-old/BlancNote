title: Dependency Inversion Principle
date: 2014-04-18
tags: [CleanCode]

#### Decoupling high-level use-cases/policy modules and low-level/implementation-detail modules through abstractions.

*This post is a work-in-progress*

Watch the original episode [here][1]

Let's start with an example, shall we?  
Let's assume we are building a social application, Sociale (Ha!), which posts statuses to all of user's connected social networks.  
Currently the application only supports posting to Twitter, and the application currently looks like this:

<!--

[Sociale]->[TwitterGateway|+PostStatus()]

-->

![](http://yuml.me/diagram/plain;/class/[Sociale]-%3E[TwitterGateway%7C+PostStatus(\)])

Here we have built a gateway to segregate and localize code that interacts with external components/applications/platforms.

This architecture looks perfectly fine, for now. 
Next we need to implement posting to Facebook, after which our application would probably look like.


<!--

[Sociale]->[TwitterGateway|+PostStatus()]
[Sociale]->[FacebookGateway|+PostStatus()]

-->

![](http://yuml.me/diagram/plain;/class/[Sociale]-%3E[TwitterGateway%7C+PostStatus(\)],[Sociale]-%3E[FacebookGateway%7C+PostStatus(\)])

Here, we realize that there seems to be an implicit understanding that FacebookGateway implements a method PostStatus() just like TwitterGateway.
As we keep on integrating social networks, if there aren't too many already, we realize that Sociale application is now tightly coupled with these gateways.  
**Hmmm... Sociale now has compile-time/source code dependency on these gateways.**

That smells.  
Sociale has an obvious runtime dependency on these gateways.  
But does that need to translate to compile-time dependency?
In other words, if a team makes changes to TwitterGateway, do we need to recompile Sociale?

How do we fix this?
**We create an interface SocialNetworkInteractor**

This interface would define all methods that need to be implemented by the gateways.
And any gateway that implements this interface can be plugged in to our application, Sociale.

Gateways are now *plugins* to our application, which would look like this:

<!--

[Sociale]PostStatus() -.-> [<<SocialNetworkInteractor>>;PostStatus()]
[<<SocialNetworkInteractor>>;PostStatus()]^-.-[FacebookGateway%7C+PostStatus(\)],[<<SocialNetworkInteractor>>;PostStatus()]^-.-[TwitterGateway%7C+PostStatus(\)],[<<SocialNetworkInteractor>>;PostStatus()]^-.-[AnotherSocialNetworkGateway%7C+PostStatus(\)]

-->
![](http://yuml.me/diagram/plain;/class/[Sociale]PostStatus(\)%20-.-%3E%20[%3C%3CSocialNetworkInteractor%3E%3E;PostStatus(\)],%20[%3C%3CSocialNetworkInteractor%3E%3E;PostStatus(\)]%5E-.-[FacebookGateway%7C+PostStatus(\)],[%3C%3CSocialNetworkInteractor%3E%3E;PostStatus(\)]%5E-.-[TwitterGateway%7C+PostStatus(\)],[%3C%3CSocialNetworkInteractor%3E%3E;PostStatus(\)]%5E-.-[AnotherSocialNetworkGateway%7C+PostStatus(\)])

Gateways now have a compile time dependency on the interface, which is **in opposite direction** to run-time dependency of Sociale Application on the gateways. 
**That is Dependency Inversion Principle (DIP).**

DIP helps us create boundaries between components, between teams (that is a good thing if done right).  
Team developing Sociale application can release code updates to code as long as the interface does not change.  
Teams developing gateways, aka plugins, can release code as long as they implement the interface.  


[1]: http://cleancoders.com/episode/clean-code-episode-13/show
[2]: http://www.teradatatips.com/
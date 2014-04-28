title: Interface Segregation Principle
date: 2014-04-22
tags: [CleanCode]

#### Don't depend on things you don't need.

*This post is a work-in-progress*

Watch the original episode [here][1]

Let's start with an example, shall we? 
Assume we are building a desktop application, Mediafy, which manages your media library.
Mediafy has a UI component, MediafyPlayerController, which has responsibility of interacting with the user.

Currently, our application only supports audio and application looks something like this:

<!--

[MediafyPlayerController]PostStatus() -.-> [<<SocialNetworkInteractor>>;PostStatus()]
[<<SocialNetworkInteractor>>;PostStatus()]^-.-[FacebookGateway%7C+PostStatus(\)],[<<SocialNetworkInteractor>>;PostStatus()]^-.-[TwitterGateway%7C+PostStatus(\)],[<<SocialNetworkInteractor>>;PostStatus()]^-.-[AnotherSocialNetworkGateway%7C+PostStatus(\)]

-->
![](http://yuml.me/diagram/plain;/class/[Sociale]PostStatus(\)%20-.-%3E%20[%3C%3CSocialNetworkInteractor%3E%3E;PostStatus(\)],%20[%3C%3CSocialNetworkInteractor%3E%3E;PostStatus(\)]%5E-.-[FacebookGateway%7C+PostStatus(\)],[%3C%3CSocialNetworkInteractor%3E%3E;PostStatus(\)]%5E-.-[TwitterGateway%7C+PostStatus(\)],[%3C%3CSocialNetworkInteractor%3E%3E;PostStatus(\)]%5E-.-[AnotherSocialNetworkGateway%7C+PostStatus(\)])



Recommended reading

* [Article on ObjectMentor][2]
* [Question on StackOverflow][3]



[1]: http://cleancoders.com/episode/clean-code-episode-12/show
[2]: http://www.objectmentor.com/resources/articles/isp.pdf
[3]: http://stackoverflow.com/questions/9249832/interface-segregation-principle-program-to-an-interface
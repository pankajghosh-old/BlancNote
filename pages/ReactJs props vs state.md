title: Why lognormal returns?
date: 2014-09-18
tags: [Untagged]

React JS: props vs state

*This post is a work-in-progress*

> React is a JavaScript library for creating user interfaces by Facebook and Instagram. Many people choose to think of React as the V in MVC.

> We built React to solve one problem: **building large applications with data that changes over time.**

[Why React?](http://facebook.github.io/react/docs/why-react.html)

React lets you design interfaces using reusable components and encourages component hierarchy.As you are creating the components, it becomes imperative to decide how they interact with each other.

There are 2 basic rules to follow:

 * Component's state should be reserved for user interaction. If your webpage (or a component) is static, it should not have any state.
 * Data flows only in one direction.

Let's take an example of a button which changes color on click

```JSX
var Button = React.createClass({
  render: function() {
    return (
      <a className="btn btn-default">button</a>
      );
  }
});
```
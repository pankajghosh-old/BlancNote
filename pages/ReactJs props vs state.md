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

Let's take an example of a button

```JSX
var Button = React.createClass({
  render: function() {
    return (
      <a className="btn btn-default">button 1</a>
      );
  }
});

React.renderComponent(
  <Button/>,
  document.body
  );
```

We will now try to add interactivity to this component. If user clicks this button, it should show as selected.
We need to to change the class of this component on click. From Rule 1, it is time we add state to this component.

```JSX
var Button = React.createClass({
  getInitialState: function() {
  	return {
  		button_class:"btn btn-default"
  	};
  },
  render: function() {
    return (
      <a className={this.state.button_class} onClick={this.handleClick}>button 1</a>
      );
  },
  handleClick: function(e){
  	this.setState({button_class:"btn btn-success"})
  }

});

React.renderComponent(
  <Button/>,
  document.body
  );
```

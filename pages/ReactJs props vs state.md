title: "ReactJS: props vs state"
date: 2014-09-18
tags: [ReactJS]

*This post is a work-in-progress*

> React is a JavaScript library for creating user interfaces by Facebook and Instagram. Many people choose to think of React as the V in MVC.

> We built React to solve one problem: **building large applications with data that changes over time.**

[Why React?](http://facebook.github.io/react/docs/why-react.html)

React lets you design interfaces using reusable components and encourages component hierarchy. And with increasing complexity of UI, designing how components interact with each other becomes imperative.

Let's jump straight into it...

Below is an example of a `Button` class with just one method: `render()`. `React.renderComponent()` replaces the DOM node, in this case `document.body`, with an instance of `Button` component.

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

Pretty simple, huh?   
Though that is one boring button, so lets make it user interactive.   
If user clicks this button, it should show as selected.

We need to to change the class of this component (from `btn-default` to `btn-success`) on a user click. It is time we add state to this component.   

React provides us with 2 main methods to handle state of any component:

 * `getInitialState`: This method, as the name suggests, is responsible for setting up initial state of the component. This method is guarenteed to be executed once during a component's lifecycle.
 * `setState`: Use this method to modify state of the component. Leave it to React to re-render the component whenever state gets updated, as we shall see below.

We add a plain old event handler `handleClick` which modifies the state of the component.

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

`Button` component's `className` is now dynamic and changes with the state `button_class` of the component.  
This button stays selected once clicked, we want the selection state to toggle with user click.

React offers a utility function `classSet` ([read about it here](http://facebook.github.io/react/docs/class-name-manipulation.html)) to manipulate `className` of any component.
We have changed the state of the component to `isSelected` which gets toggled on event `onClick` cascading to a change in class of the component itself.

    var Button = React.createClass({
      getInitialState: function() {
        return {
          isSelected:false
        };
      },
      render: function() {
        var classes = React.addons.classSet({
          'btn': true,
          'btn-default': ! this.state.isSelected,
          'btn-success': this.state.isSelected,
        });
        return (
          <a className={classes} onClick={this.handleClick}>button 1</a>
          );
      },
      handleClick: function(e){
        this.setState({isSelected:! this.state.isSelected})
      }

    });

    React.renderComponent(
      <Button/>,
      document.body
      );

[Continued here...](/../ReactJs props vs state - Continued)
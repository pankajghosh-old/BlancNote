title: "ReactJS: props vs state"
date: 2014-09-18
tags: [Untagged]

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
Though that is one boring button, so lets add user interactivity to it.   
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

We will try to add a small update to above component before we move on to more complex scenario.
Currently, behavior of the button is that is stays selected once done. 
We would like the button's selection to act like toggle.


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

To display interactivity between components, let's create a dynamic list of boxes.

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
          <a className={classes} onClick={this.handleClick}>button {this.props.index+1}</a>
          );
      },
      handleClick: function(e){
        this.setState({isSelected:! this.state.isSelected})
      }

    });

    var ButtonList = React.createClass({
        render:function(){
            var buttons = [];
            for(var i = 0; i < 5; i++) {
                buttons.push(<Button index={i}/>);
            }
            return (
            <div>
                {buttons}
            </div>
            )        
        }

    });

    React.renderComponent(
      <ButtonList count={5}/>,
      document.body
      );


The problem we would now try to solve is that we want to deselect other buttons as buttons are clicked.

    var Button = React.createClass({
      render: function() {
        var classes = React.addons.classSet({
          'btn': true,
          'btn-default': ! this.props.isSelected,
          'btn-success': this.props.isSelected,
        });
        return (
          <a className={classes}>{this.props.buttonName}</a>
          );
      }

    });

    var ButtonList = React.createClass({
        getInitialState:function(){
            return {selectedButton:""}
        },
        render:function(){
            var buttons = [];
            var that = this;
            for(var i = 0; i < 5; i++) {
                var buttonName = "Button "+(i+1);
                var isSelected = buttonName===that.state.selectedButton;
                buttons.push(<Button buttonName={buttonName} isSelected={isSelected}/>);
            }
            return (
            <div onClick={this.handleClick}>
                {buttons}
            </div>
            )        
        },
        handleClick:function(e){
            this.setState({selectedButton:e.target.text})
        }

    });

    React.renderComponent(
      <ButtonList count={5}/>,
      document.body
      );

There are 3 basic guidelines, which I have found helpful, while creating components:

 * **Component's `state` should be reserved for user interaction**: If your webpage (or a component) is static, it should not have any state.
 * **A component modifies another component via its `props`**: `props` on the other hand are immutable, a component's parent owns them. In a lot of cases, parent's `state` would include child components' `props`.
 * Data flows only in one direction:

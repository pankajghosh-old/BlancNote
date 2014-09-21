title: React JS props vs state
date: 2014-09-18
tags: [Untagged]

*This post is a work-in-progress*

> React is a JavaScript library for creating user interfaces by Facebook and Instagram. Many people choose to think of React as the V in MVC.

> We built React to solve one problem: **building large applications with data that changes over time.**

[Why React?](http://facebook.github.io/react/docs/why-react.html)

React lets you design interfaces using reusable components and encourages component hierarchy.As you are creating the components, it becomes imperative to decide how they interact with each other.

There are 2 basic rules to follow:

 * Component's state should be reserved for user interaction. If your webpage (or a component) is static, it should not have any state.
 * Data flows only in one direction.

Let's take an example of a button

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

We will now try to add interactivity to this component. If user clicks this button, it should show as selected.
We need to to change the class of this component on click. From Rule 1, it is time we add state to this component.

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
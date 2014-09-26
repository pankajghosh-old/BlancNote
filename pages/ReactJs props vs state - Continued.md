title: "ReactJS: props vs state - Continued"
date: 2014-09-18
tags: [ReactJS]

*This post is a work-in-progress*


To display interactivity between components, we would need more than one component so let's create a list of buttons. `ButtonList` passes a prop `index` to each `Button` and now we have five buttons each with different text and each responding to click events by themselves. `ButtonList` here is no more than a container for the list of 5 `Button` instances.

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

import React from 'react';


export default class IngredientTable extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            count: 0
        };
        this.addIngredient = this.addIngredient.bind(this);
    }
    addIngredient(){
        console.log(this.state.count);
        this.setState({
            count: this.state.count + 1
        });
    }
    render() {
        return (
            <button id={"test"} onClick={this.addIngredient}>Click Me! -> {this.state.count}</button>
        )
    }
}
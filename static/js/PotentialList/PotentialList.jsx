import React from 'react';


export default class PotentialList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            count: 0
        };
        this.setCount = this.setCount.bind(this);
    }
    setCount(){
        this.setState({
            count: document.getElementById("test").innerText
        });
    }
    render() {
        return (
            <div>
                <button onClick={this.setCount}>Click Me!</button>
                <ul>
                    <li>{this.state.count}</li>
                </ul>
            </div>
        );
    }
}
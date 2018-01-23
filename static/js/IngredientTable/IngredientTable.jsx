import React from 'react';
import IngredientRow from './IngredientRow/IngredientRow';
import { Table } from 'react-bootstrap';


const ingredientsRequest = new window.Request('http://127.0.0.1:5000/api/Ingredients',
    {method: 'GET', dataType: 'json'});



export default class IngredientTable extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            ingredients: new Array([])
        };
        this.componentDidMount = this.componentDidMount.bind(this);
    }
    componentDidMount(){
        window.fetch(ingredientsRequest)
            .then(response => {
                if (response.status === 200) {
                    return response.json();
                } else {
                    throw new Error('Something went wrong requesting Ingredients!');
                }
            })
            .then(data => {
                this.setState({ingredients: data.objects });
            });
    }
    render() {
        const ingredients = this.state.ingredients;
        let key = 0;
        return (
            <Table >
                <thead><tr><th>Ingredient</th><th>Count</th><th>Potion Preference</th></tr></thead>
                <tbody>
                    {ingredients.map(function(ingredient) {
                        key += 1;
                        return (
                            <IngredientRow key={key} ingredient={ingredient}/>
                        )
                    })}
                </tbody>
            </Table>
        )
    }
}
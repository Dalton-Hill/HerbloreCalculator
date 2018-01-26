import React from 'react';
import IngredientRow from './IngredientRow/IngredientRow';
import { Table } from 'react-bootstrap';


export default class IngredientTable extends React.Component {
    constructor(props){
        super(props);
        let ingredients = this.props.ingredients;
        if (ingredients === undefined) {
            ingredients = new Array([])
        }
        this.state = {
            ingredients: ingredients
        }
    }
    componentWillReceiveProps(nextProps){
        this.setState({ingredients: nextProps.ingredients})
    }
    render() {
        const ingredients = this.state.ingredients;
        const parentUpdateIngredientCount = this.props.parentUpdateIngredientCount;
        const parentUpdatePotionPreference = this.props.parentUpdatePotionPreference;
        let key = 0;
        return (
            <Table className={"table table-bordered"}>
                <thead><tr><th>Ingredient</th><th>Count</th><th>Potion Preference</th></tr></thead>
                <tbody>
                    {ingredients.map(function(ingredient) {
                        key += 1;
                        return (
                            <IngredientRow key={key} rowKey={key} ingredient={ingredient}
                            parentUpdateIngredientCount={parentUpdateIngredientCount}
                            parentUpdatePotionPreference={parentUpdatePotionPreference}/>
                        )
                    })}
                </tbody>
            </Table>
        )
    }
}
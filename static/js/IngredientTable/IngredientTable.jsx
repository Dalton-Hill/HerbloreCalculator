import React from 'react';
import IngredientRow from './IngredientRow/IngredientRow';
import { Table } from 'react-bootstrap';


export default class IngredientTable extends React.Component {
    render() {
        let ingredients = this.props.ingredients;
        let potions = this.props.potions;
        if(ingredients === undefined) ingredients = [];
        if(potions === undefined) potions = [];
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
                            <IngredientRow key={key} rowKey={key} ingredient={ingredient} potions={potions}
                            parentUpdateIngredientCount={parentUpdateIngredientCount}
                            parentUpdatePotionPreference={parentUpdatePotionPreference}/>
                        )
                    })}
                </tbody>
            </Table>
        )
    }
}
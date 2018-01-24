import React from 'react';
import IngredientNameColumn from './Columns/IngredientNameColumn'
import IngredientCountColumn from './Columns/IngredientCountColumn'
import PotionPreferenceColumn from './Columns/PotionPreferenceColumn'




export default class IngredientRow extends React.Component {
    render() {
        return (
            <tr ingredient-id={this.props.ingredient.id}>
                <IngredientNameColumn key={1} name={this.props.ingredient.name}/>
                <IngredientCountColumn key={2}/>
                <PotionPreferenceColumn key={3} rowKey={this.props.rowKey} potions={this.props.ingredient.potions}/>
            </tr>
        );
    }
}
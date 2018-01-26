import React from 'react';
import IngredientNameColumn from './Columns/IngredientNameColumn'
import IngredientCountColumn from './Columns/IngredientCountColumn'
import PotionPreferenceColumn from './Columns/PotionPreferenceColumn'




export default class IngredientRow extends React.Component {
    render() {
        return (
            <tr ingredient-id={this.props.ingredient.id}>
                <IngredientNameColumn key={1} name={this.props.ingredient.name}/>
                <IngredientCountColumn parentUpdateIngredientCount={this.props.parentUpdateIngredientCount}
                                       key={2} ingredient={this.props.ingredient}/>
                <PotionPreferenceColumn key={3} ingredient={this.props.ingredient}
                                        parentUpdatePotionPreference={this.props.parentUpdatePotionPreference}/>
            </tr>
        );
    }
}
import React from 'react';
import IngredientNameColumn from './Columns/IngredientNameColumn'
import IngredientCountColumn from './Columns/IngredientCountColumn'
import PotionPreferenceColumn from './Columns/PotionPreferenceColumn'




export default class IngredientRow extends React.Component {
    render() {
        return (
            <tr>
                <IngredientNameColumn key={this.key} name={this.props.ingredient.name}/>
                <IngredientCountColumn key={this.key}/>
                <PotionPreferenceColumn key={this.key}/>
            </tr>
        );
    }
}
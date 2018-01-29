import React from 'react';
import { FormGroup, ControlLabel, FormControl } from 'react-bootstrap';


export default class PotionPreferenceColumn extends React.Component {
    render() {
        const parentUpdatePotionPreference = this.props.parentUpdatePotionPreference;
        let ingredient = this.props.ingredient;
        const all_potions = this.props.potions;
        let potion_options = [];

        if(!(ingredient.potion_ingredients === undefined) && !(all_potions === undefined)){
            const ingredient_potions = ingredient.potion_ingredients.map(pi => pi.potion_id);
            all_potions.map(function(potion){
                if(ingredient_potions.indexOf(potion.id) !== -1){
                    potion_options.push(potion);
                }
            })
        }

        let key = 0;
        return (
            <td className={"PotionPreferenceColumn"}>
                <FormGroup controlId={"formControlsSelect"}>
                    <FormControl componentClass={"select"} placeholder={"select"}
                                 ingredient-id={ingredient.id} onChange={parentUpdatePotionPreference}>
                        <option key={key} value={0} potion-ingredients={[]}>Choose a Potion</option>
                        {potion_options.map(function(potion) {
                            key += 1;
                            return (
                                <option
                                    key={key}
                                    value={potion.id}
                                    potion-ingredients={potion.ingredients}
                                >{potion.name}
                                </option>
                            )
                        })}
                    </FormControl>
                </FormGroup>
            </td>
        )
    }
}
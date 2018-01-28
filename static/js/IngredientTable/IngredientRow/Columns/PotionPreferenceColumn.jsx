import React from 'react';
import { FormGroup, ControlLabel, FormControl } from 'react-bootstrap';


export default class PotionPreferenceColumn extends React.Component {
    constructor(props){
        super(props);
        let potions = this.props.ingredient.potions;
        if (potions === undefined) {
            potions = new Array([])
        }
        this.state = {
            potions: potions
        };
    }
    componentWillReceiveProps(nextProps){
        this.setState({potions: nextProps.ingredient.potions})
    }
    render() {
        const parentUpdatePotionPreference = this.props.parentUpdatePotionPreference;
        let key = 0;
        return (
            <td className={"PotionPreferenceColumn"}>
                <FormGroup controlId={"formControlsSelect"}>
                    <FormControl componentClass={"select"} placeholder={"select"}
                                 ingredient-id={this.props.ingredient.id} onChange={parentUpdatePotionPreference}>
                        <option key={key} value={0} potion-ingredients={[]}>Choose a Potion</option>
                        {this.state.potions.map(function(potion) {
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
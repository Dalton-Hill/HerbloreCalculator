import React from 'react';
import { FormGroup, ControlLabel, FormControl } from 'react-bootstrap';


export default class PotionPreferenceColumn extends React.Component {
    constructor(props){
        super(props);
        let potions = this.props.potions;
        if (potions === undefined) {
            potions = new Array([])
        }
        this.state = {
            potions: potions
        }
    }
    componentWillReceiveProps(nextProps){
        this.setState({potions: nextProps.potions})
    }
    render() {
        return (
            <td className={"PotionPreferenceColumn"}>
                <FormGroup controlId={"formControlsSelect"}>
                    <FormControl componentClass={"select"} placeholder={"select"}>
                        <option potion-id={null}>Choose a Potion</option>
                        {this.state.potions.map(function(potion) {
                            return (
                                <option
                                    potion-id={potion.id}
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
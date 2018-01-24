import React from 'react';
import { DropdownButton, MenuItem } from 'react-bootstrap';


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
        const rowKey = this.props.rowKey;
        let key = 0;
        return (
            <td className={"PotionPreferenceColumn"}>
                <DropdownButton bsStyle={"default"} title={"Choose a Potion"} key={rowKey} id={'Dropdown' + rowKey}>
                    {this.state.potions.map(function(potion) {
                        key += 1;
                        return (
                            <MenuItem key={key} potion-id={potion.id}>{potion.name}
                            </MenuItem>
                        )
                    })}
                </DropdownButton>
            </td>
        )
    }
}
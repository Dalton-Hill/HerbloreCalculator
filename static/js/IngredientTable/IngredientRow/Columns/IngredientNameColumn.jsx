import React from 'react';


export default class IngredientNameColumn extends React.Component {
    render() {
        return (
            <td className={"IngredientNameColumn"}>{this.props.name}</td>
        )
    }

}
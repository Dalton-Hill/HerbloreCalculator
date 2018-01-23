import React from 'react';


export default class IngredientCountColumn extends React.Component {
    render() {
        return (
            <td className={"IngredientCountColumn"}>
                <input placeholder={0}></input>
            </td>
        )
    }

}
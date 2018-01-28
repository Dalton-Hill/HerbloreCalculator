import React from 'react';


export default class ResultRow extends React.Component{
    render(){
        return (
            <tr>
                <td className={"PotionName"}>{this.props.potion.name}</td>
                <td className={"PotionCount"}>{this.props.potion.count}</td>
                <td className={"PotionExperience"}>{this.props.potion.totalExperience}</td>
            </tr>
            )
    }
}
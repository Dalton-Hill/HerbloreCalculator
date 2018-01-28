import React from 'react';


const calculateExperience = (potion) => potion.xp_reward * potion.count;


export default class ResultRow extends React.Component{
    render(){
        return (
            <tr>
                <td className={"PotionName"}>{this.props.potion.name}</td>
                <td className={"PotionCount"}>{this.props.potion.count}</td>
                <td className={"PotionExperience"}>{calculateExperience(this.props.potion)}</td>
            </tr>
            )
    }
}
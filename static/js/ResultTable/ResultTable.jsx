import React from 'react';
import { Table } from 'react-bootstrap';


const defaultPotionCountsToZero = (potions) => {
    for(let i = 0; i < potions.length; i++){
        potions[i].count = 0;
        for(let x = 0; x < potions[i].ingredients.length; x++){
            potions[i].ingredients[x].count = 0;
        }
    }
    return potions.slice();
};


const calculatePossiblePotions = (ingredients, potions) => {
    if(potions.length > 1){
        potions = defaultPotionCountsToZero(potions);
        for(let i = 0; i < potions.length; i++){
            for(let x = 0; x < ingredients.length; x++){
                for(let y = 0; y < potions[i].ingredients.length; y++){
                    if(potions[i].ingredients[y].id === ingredients[x].id && potions[i].id === ingredients[x].potionPreferenceId){
                        potions[i].ingredients[y].count = ingredients[x].count;
                    }
                }
            }
            potions[i].count = 0;
            let ingredientsCount = [];
            for(let z = 0; z < potions[i].ingredients.length; z++){
                ingredientsCount.push(potions[i].ingredients[z].count)
            }
            let count = Math.min(...ingredientsCount);
            if(isNaN(count)){
                count = 0
            }
            potions[i].count = count;
        }
    }
    console.log(potions);
    return(potions);
};


export default class ResultTable extends React.Component{
    render(){
        calculatePossiblePotions(this.props.ingredients.slice(), this.props.potions.slice());
        return(
            <Table className={"table table-bordered"}>
                <thead><tr><th>Potion</th><th>Count</th><th>Experience</th></tr></thead>
            </Table>
        );
    }
}
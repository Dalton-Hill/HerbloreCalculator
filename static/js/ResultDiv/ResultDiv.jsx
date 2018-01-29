import React from 'react';
import { Table, FormGroup, ControlLabel, FormControl} from 'react-bootstrap';
import ResultRow from './ResultRow/ResultRow'


const calculateTotalExperience = (potions) => {
    let totalExperience = 0;
    if (potions.length > 1){
        for(let i = 0; i < potions.length; i++){
            totalExperience += potions[i].totalExperience;
        }
    }
    return totalExperience;
};


const calculateExperience = (potion) => potion.xp_reward * potion.count;


const defaultPotionCountsToZero = (potions) => {
    for(let i = 0; i < potions.length; i++){
        potions[i].count = 0;
        for(let x = 0; x < potions[i].potion_ingredients.length; x++){
            potions[i].potion_ingredients[x].count = 0;
        }
    }
    return potions.slice();
};


const calculatePossiblePotions = (ingredients, potions) => {
    if(potions.length > 1){
        potions = defaultPotionCountsToZero(potions);
        for(let i = 0; i < potions.length; i++){
            for(let x = 0; x < ingredients.length; x++){
                for(let y = 0; y < potions[i].potion_ingredients.length; y++){
                    if(potions[i].potion_ingredients[y].ingredient_id === ingredients[x].id && potions[i].id === ingredients[x].potionPreferenceId){
                        potions[i].potion_ingredients[y].count = Math.floor(ingredients[x].count / potions[i].potion_ingredients[y].ingredients_per_potion);
                    }
                }
            }
            potions[i].count = 0;
            let ingredientsCount = [];
            for(let z = 0; z < potions[i].potion_ingredients.length; z++){
                ingredientsCount.push(potions[i].potion_ingredients[z].count)
            }
            let count = Math.min(...ingredientsCount);
            if(isNaN(count)){
                count = 0
            }
            potions[i].count = count;
            potions[i].totalExperience = calculateExperience(potions[i]);
        }
    }
    return potions.slice();
};


export default class ResultDiv extends React.Component{
    render(){
        const potions = calculatePossiblePotions(this.props.ingredients.slice(), this.props.potions.slice());
        const totalExperience = calculateTotalExperience(potions);
        let key = 0;
        return(
            <div>
                <form className={"form"}>
                    <FormGroup>
                        <ControlLabel htmlFor={"totalExperience"}>Total Experience</ControlLabel>
                        <FormControl.Static id={"totalExperience"}>{totalExperience}</FormControl.Static>
                    </FormGroup>
                </form>
                <Table className={"table table-bordered"}>
                    <thead><tr><th>Potion</th><th>Count</th><th>Experience</th></tr></thead>
                    <tbody>
                        {potions.map(function(potion){
                            if(potion.count > 0){
                                key += 1;
                                return(
                                    <ResultRow
                                        key={key}
                                        potion={potion}
                                    >
                                    </ResultRow>
                                )
                            }
                        })}
                    </tbody>
                </Table>
            </div>
        );
    }
}
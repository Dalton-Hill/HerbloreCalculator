import React from "react";
import IngredientTable from './IngredientTable/IngredientTable';
import ResultDiv from './ResultDiv/ResultDiv'


// const ip_address = "http://localhost:5000"; // LOCAL
const ip_address = "http://herb-calc-lb-1887002446.us-east-1.elb.amazonaws.com"; // PRODUCTION


const ingredientsRequest = new window.Request(ip_address + '/api/Ingredients',
    {method: 'GET', dataType: 'json'});
const potionsRequest = new window.Request(ip_address + '/api/Potions',
    {method: 'GET', dataType: 'json'});


export default class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            ingredients: new Array([]),
            potions: new Array([]),
        };
        this.updateIngredientCount = this.updateIngredientCount.bind(this);
        this.updatePotionPreference = this.updatePotionPreference.bind(this);
        this.fetchIngredients = this.fetchIngredients.bind(this);
        this.fetchIngredients();
        this.fetchPotions = this.fetchPotions.bind(this);
        this.fetchPotions();
    }
    fetchIngredients(){
        window.fetch(ingredientsRequest)
            .then(response => {
                if (response.status === 200) {
                    return response.json();
                } else {
                    throw new Error('Something went wrong requesting Ingredients!');
                }
            })
            .then(data => {
                let ingredients = data.objects;
                for (let i = 0; i < ingredients.length; i++){
                    ingredients[i].count = 0;
                    if(ingredients[i].potion_ingredients.length === 1){
                        ingredients[i].potionPreferenceId = ingredients[i].potion_ingredients[0].potion_id;
                    } else {
                        ingredients[i].potionPreferenceId = 0;
                    }
                }
                this.setState({ingredients: ingredients});
            });
    }
    fetchPotions(){
        window.fetch(potionsRequest)
            .then(response => {
                if (response.status === 200) {
                    return response.json();
                } else {
                    throw new Error('Something went wrong requesting Potions!');
                }
            })
            .then(data => {
                let potions = data.objects;
                for (let i = 0; i < potions.length; i++){
                    potions[i].count = 0;
                    const potion_ingredients = potions[i].potion_ingredients;
                    for (let x = 0; x < potion_ingredients.length; x++){
                        potion_ingredients[x].count = 0;
                    }
                }
                this.setState({potions: potions});
            });
    }
    updateIngredientCount(e){
        const ingredient_id = parseInt(e.target.getAttribute("ingredient-id"));
        let count = parseInt(e.target.value);
        let ingredients = this.state.ingredients.slice();
        if(isNaN(count)){
            count = 0;
        }
        for (let i = 0; i < ingredients.length; i++){
            if (ingredient_id === ingredients[i].id){
                ingredients[i].count = count;
                break
            }
        }
        this.setState({ingredients: ingredients});
    }
    updatePotionPreference(e){
        const ingredient_id = parseInt(e.target.getAttribute("ingredient-id"));
        const potion_id = parseInt(e.target.value);
        let ingredients = this.state.ingredients.slice();
        for (let i = 0; i < ingredients.length; i++){
            if (ingredient_id === ingredients[i].id){
                ingredients[i].potionPreferenceId = potion_id;
                break
            }
        }
        this.setState({ingredients: ingredients});
    }
    render() {
        return (
            <div className={"Container"}>
                <IngredientTable ingredients={this.state.ingredients}
                                 potions={this.state.potions}
                                 parentUpdateIngredientCount={this.updateIngredientCount}
                                 parentUpdatePotionPreference={this.updatePotionPreference}
                />
                <ResultDiv potions={this.state.potions} ingredients={this.state.ingredients}/>
            </div>
        );
    }
}
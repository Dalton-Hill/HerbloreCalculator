import React from "react";
import IngredientTable from './IngredientTable/IngredientTable';
import PotentialList from './PotentialList/PotentialList';


const ingredientsRequest = new window.Request('http://127.0.0.1:5000/api/Ingredients',
    {method: 'GET', dataType: 'json'});


export default class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            ingredients: new Array([])
        };
        this.updateIngredientCount = this.updateIngredientCount.bind(this);
        this.fetchIngredients = this.fetchIngredients.bind(this);
        this.fetchIngredients();
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
                }
                this.setState({ingredients: ingredients });
            });
    }
    updateIngredientCount(e){
        const ingredient_id = e.target.getAttribute("ingredient-id");
        const count = e.target.value;
        let ingredients = this.state.ingredients;
        console.log('called');
        console.log(ingredient_id);
        console.log(count);
        for (let i = 0; i < ingredients.length; i++){
            if (ingredient_id === ingredients[i].id){
                ingredients[i].count = count;
                console.log(count);
                break
            }
        }
        this.setState({ingredients: ingredients})
    }
    render() {
        return (
            <div className={"Container"}>
                <IngredientTable ingredients={this.state.ingredients}
                                 parentUpdateIngredientCount={this.updateIngredientCount}/>
                <PotentialList />
            </div>
        );
    }
}
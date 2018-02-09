import React from 'react';
import IngredientRow from './IngredientRow/IngredientRow';
import { Table, Button } from 'react-bootstrap';


export default class IngredientTable extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            ingredients: props.ingredients,
            potions: props.potions,
            ingredient_herbs: [],
            ingredient_secondaries: [],
            ingredient_potions: [],
            ingredient_herbs_visible: false,
            ingredient_secondaries_visible: false,
            ingredient_potions_visible: false,
        };
        this.toggleIngredientType = this.toggleIngredientType.bind(this);
    }
    componentWillReceiveProps(newProps){
        this.setState({
                    ingredients: newProps.ingredients,
                    potions: newProps.potions
                });
    }
    toggleIngredientType(e){
        const nameOfStateClicked = e.target.getAttribute('name-of-st');
        const list_to_update = nameOfStateClicked.replace('_visible', '');
        const display = !this.state[nameOfStateClicked];
        this.setState({
        });
        let new_list = [];
        if(this.state.ingredients.length > 1){
            for(let i = 0;i < this.state.ingredients.length; i++){
                if(this.state.ingredients[i].ingredient_type.name.toLowerCase() === 'herb' && nameOfStateClicked === 'ingredient_herbs_visible' && display === true){
                    new_list.push(this.state.ingredients[i])
                } else if(this.state.ingredients[i].ingredient_type.name.toLowerCase() === 'secondary' && nameOfStateClicked === 'ingredient_secondaries_visible' && display === true){
                    new_list.push(this.state.ingredients[i])
                } else if(this.state.ingredients[i].ingredient_type.name.toLowerCase() === 'potion' && nameOfStateClicked === 'ingredient_potions_visible' && display === true){
                    new_list.push(this.state.ingredients[i]);
                }
            }
            const sortByName = (a, b) => {
                const aName = a.name.toLowerCase();
                const bName = b.name.toLowerCase();
                if(aName < bName) return -1;
                return 1;
            };
            new_list.sort(sortByName);
            this.setState({ // blah i hope this works but we shall see
                [list_to_update]: new_list,
                [nameOfStateClicked]: !this.state[nameOfStateClicked]
            });
        }
    }
    render() {
        const parentUpdateIngredientCount = this.props.parentUpdateIngredientCount;
        const parentUpdatePotionPreference = this.props.parentUpdatePotionPreference;
        let key = 0;
        const potions = this.state.potions;
        return (
            <Table className={"table table-bordered"}>
                <thead><tr><th>Ingredient</th><th>Count</th><th>Potion Preference</th></tr></thead>
                <tbody id={'ingredient_table'}>
                <tr><td><Button bsStyle={'success'} id={'showHerbsButton'} name-of-st={"ingredient_herbs_visible"} onClick={this.toggleIngredientType}>Toggle Herbs</Button></td><td></td><td></td></tr>
                    {this.state.ingredient_herbs.map(function(ingredient) {
                        key += 1;
                        return (
                            <IngredientRow key={key} rowKey={key} ingredient={ingredient} potions={potions}
                            parentUpdateIngredientCount={parentUpdateIngredientCount}
                            parentUpdatePotionPreference={parentUpdatePotionPreference}/>
                        )
                    })}
                <tr><td><Button bsStyle={'info'} id={'showSecondariesButton'} name-of-st={"ingredient_secondaries_visible"} onClick={this.toggleIngredientType}>Toggle Secondaries</Button></td><td></td><td></td></tr>
                    {this.state.ingredient_secondaries.map(function(ingredient) {
                        key += 1;
                        return (
                            <IngredientRow key={key} rowKey={key} ingredient={ingredient} potions={potions}
                            parentUpdateIngredientCount={parentUpdateIngredientCount}
                            parentUpdatePotionPreference={parentUpdatePotionPreference}/>
                        )
                    })}
                <tr><td><Button bsStyle={'warning'} id={'showIngredientPotionsButton'} name-of-st={"ingredient_potions_visible"} onClick={this.toggleIngredientType}>Toggle Ingredient Potions</Button></td><td></td><td></td></tr>
                    {this.state.ingredient_potions.map(function(ingredient) {
                        key += 1;
                        return (
                            <IngredientRow key={key} rowKey={key} ingredient={ingredient} potions={potions}
                            parentUpdateIngredientCount={parentUpdateIngredientCount}
                            parentUpdatePotionPreference={parentUpdatePotionPreference}/>
                        )
                    })}
                </tbody>
            </Table>
        )
    }
}
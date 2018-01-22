import React from "react";
import IngredientTable from './IngredientTable/IngredientTable';
import PotentialList from './PotentialList/PotentialList';


export default class App extends React.Component {
    render() {
        return (
            <div >
                <IngredientTable />
                <PotentialList />
            </div>
        );
    }
}
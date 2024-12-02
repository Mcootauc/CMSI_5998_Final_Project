import React, { useState } from 'react';
import HomePage from './components/HomePage';
import './App.css';

const App = () => {
    const [places, setPlaces] = useState([]);

    const fetchPlaces = (filters) => {
        console.log('Fetching places with filters:', filters);
        // Add API calls here using the filters
        setPlaces([
            {
                Name: 'Tilt Coffee Bar',
                Address: '334 S Main St, Los Angeles, CA 90013',
                Category: 'Coffee Shop',
            },
        ]);
    };

    return <HomePage places={places} onApplyFilters={fetchPlaces} />;
};

export default App;

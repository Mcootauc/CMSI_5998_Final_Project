import React from 'react';
import FiltersSection from './FiltersSection';
import ExploreSection from './ExploreSection';
import '../styles/HomePage.css';

const HomePage = () => {
    return (
        <div className="homepage">
            <header className="homepage-header">
                <h1>Urban Explorer</h1>
                <p>Discover events, places, and activities in your city!</p>
            </header>
            <FiltersSection />
            <ExploreSection />
        </div>
    );
};

export default HomePage;

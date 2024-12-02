import React from 'react';
import PlaceCard from './PlaceCard';
import '../styles/ExploreSection.css';

const ExploreSection = ({ places }) => {
    return (
        <div className="explore-section">
            {places && places.length > 0 ? (
                places.map((place, index) => (
                    <PlaceCard key={index} place={place} />
                ))
            ) : (
                <p>No places to display. Adjust your filters.</p>
            )}
        </div>
    );
};

export default ExploreSection;

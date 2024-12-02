import React from 'react';
import '../styles/PlaceCard.css';

const PlaceCard = ({ place }) => {
    return (
        <div className="place-card">
            <h3>{place.Name}</h3>
            <p>{place.Address}</p>
            <p>
                <strong>Category:</strong> {place.Category}
            </p>
        </div>
    );
};

export default PlaceCard;

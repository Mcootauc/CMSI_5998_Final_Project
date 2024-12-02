import React, { useState } from 'react';
import '../styles/FiltersSection.css';

const FiltersSection = ({ onApplyFilters }) => {
    const [query, setQuery] = useState('');
    const [category, setCategory] = useState('');
    const [location, setLocation] = useState('');

    const handleApplyFilters = () => {
        onApplyFilters({ query, category, location });
    };

    return (
        <div className="filters-section">
            <input
                type="text"
                placeholder="Search query (e.g., coffee)"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
            />
            <input
                type="text"
                placeholder="Location (e.g., Los Angeles)"
                value={location}
                onChange={(e) => setLocation(e.target.value)}
            />
            <select
                value={category}
                onChange={(e) => setCategory(e.target.value)}
            >
                <option value="">All Categories</option>
                <option value="Coffee Shop">Coffee Shop</option>
                <option value="Restaurant">Restaurant</option>
                <option value="Event">Event</option>
            </select>
            <button onClick={handleApplyFilters}>Apply Filters</button>
        </div>
    );
};

export default FiltersSection;

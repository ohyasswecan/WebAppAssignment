// src/components/GenericForm.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const GenericForm = ({ modelName, initialData, endpoint, onSubmit }) => {
    const [formData, setFormData] = useState(initialData || {});

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            if (formData.id) {
                // Update existing instance
                await axios.put(`${endpoint}/${formData.id}/`, formData);
            } else {
                // Create new instance
                await axios.post(endpoint, formData);
            }
            onSubmit();
        } catch (error) {
            console.error('Error submitting form:', error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            {Object.keys(formData).map((key) => (
                <div key={key}>
                    <label>{key}:</label>
                    <input
                        type="text"
                        name={key}
                        value={formData[key]}
                        onChange={handleChange}
                        required
                    />
                </div>
            ))}
            <button type="submit">Submit</button>
        </form>
    );
};

export default GenericForm;

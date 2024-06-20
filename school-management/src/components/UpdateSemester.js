// src/components/UpdateSemester.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams, useNavigate } from 'react-router-dom';
import Layout from './Layout';

const UpdateSemester = () => {
    const { semesterId } = useParams();
    const [semester, setSemester] = useState({
        semester_year: '',
        semester_name: '',
    });
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchSemester = async () => {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/api/semesters/${semesterId}/`);
                setSemester(response.data);
                setLoading(false);
            } catch (error) {
                console.error('Error fetching semester:', error);
                setError(error);
                setLoading(false);
            }
        };

        fetchSemester();
    }, [semesterId]);

    const handleChange = (e) => {
        setSemester({ ...semester, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.put(`http://127.0.0.1:8000/api/semesters/${semesterId}/`, semester);
            navigate('/semesters');
        } catch (error) {
            console.error('Error updating semester:', error);
            setError(error);
        }
    };

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error loading semester: {error.message}</p>;

    return (
        <Layout>
            <div>
                <h1>Update Semester</h1>
                <form onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label htmlFor="semester_year">Semester Year</label>
                        <input
                            type="number"
                            className="form-control"
                            id="semester_year"
                            name="semester_year"
                            value={semester.semester_year}
                            onChange={handleChange}
                        />
                    </div>
                    <div className="form-group">
                        <label htmlFor="semester_name">Semester Name</label>
                        <input
                            type="text"
                            className="form-control"
                            id="semester_name"
                            name="semester_name"
                            value={semester.semester_name}
                            onChange={handleChange}
                        />
                    </div>
                    <button type="submit" className="btn btn-primary">Update Semester</button>
                </form>
            </div>
        </Layout>
    );
};

export default UpdateSemester;

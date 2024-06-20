// src/components/UpdateLecturer.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams, useNavigate } from 'react-router-dom';
import Layout from './Layout';

const UpdateLecturer = () => {
    const { lecturerId } = useParams();
    const navigate = useNavigate();
    const [form, setForm] = useState({
        staff_id: '',
        lecturer_firstname: '',
        lecturer_lastname: '',
        lecturer_email: '',
        lecturer_DOB: '',
    });
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchLecturer = async () => {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/api/lecturers/${lecturerId}/`);
                setForm(response.data);
                setLoading(false);
            } catch (error) {
                console.error('Error fetching lecturer:', error);
                setError(error);
                setLoading(false);
            }
        };

        fetchLecturer();
    }, [lecturerId]);

    const handleChange = (e) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.put(`http://127.0.0.1:8000/api/lecturers/${lecturerId}/`, form);
            navigate('/lecturers');
        } catch (error) {
            console.error('Error updating lecturer:', error);
            setError(error);
        }
    };

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error: {error.message}</p>;

    return (
        <Layout>
            <div>
                <h1>Update Lecturer</h1>
                <form onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label htmlFor="lecturer_firstname">First Name</label>
                        <input
                            type="text"
                            className="form-control"
                            id="lecturer_firstname"
                            name="lecturer_firstname"
                            value={form.lecturer_firstname}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <div className="form-group">
                        <label htmlFor="lecturer_lastname">Last Name</label>
                        <input
                            type="text"
                            className="form-control"
                            id="lecturer_lastname"
                            name="lecturer_lastname"
                            value={form.lecturer_lastname}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <div className="form-group">
                        <label htmlFor="lecturer_email">Email</label>
                        <input
                            type="email"
                            className="form-control"
                            id="lecturer_email"
                            name="lecturer_email"
                            value={form.lecturer_email}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <div className="form-group">
                        <label htmlFor="lecturer_DOB">Date of Birth</label>
                        <input
                            type="date"
                            className="form-control"
                            id="lecturer_DOB"
                            name="lecturer_DOB"
                            value={form.lecturer_DOB}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <button type="submit" className="btn btn-primary">Update Lecturer</button>
                </form>
            </div>
        </Layout>
    );
};

export default UpdateLecturer;

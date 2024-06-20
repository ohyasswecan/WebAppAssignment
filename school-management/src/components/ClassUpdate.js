// src/components/ClassUpdate.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate, useParams } from 'react-router-dom';
import Layout from './Layout';

const ClassUpdate = () => {
    const { classId } = useParams();
    const [form, setForm] = useState({
        class_id: '',
        class_number: '',
        class_course: '',
        class_lecturer: '',
        class_semester: '',
    });
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchClass = async () => {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/api/class_enrollments/${classId}/`);
                setForm(response.data);
                setLoading(false);
            } catch (error) {
                console.error('Error fetching class:', error);
                setError(error);
                setLoading(false);
            }
        };

        fetchClass();
    }, [classId]);

    const handleChange = (e) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.put(`http://127.0.0.1:8000/api/class_enrollments/${classId}/`, form);
            navigate('/class_enrollments');
        } catch (error) {
            console.error('Error updating class:', error);
            setError(error);
        }
    };

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error loading class: {error.message}</p>;

    return (
        <Layout>
            <div>
                <h1>Update Class</h1>
                <form onSubmit={handleSubmit}>
                    <table className="table">
                        <thead>
                            <tr>
                                <th>#</th>
                                <th>Class ID</th>
                                <th>Class Number</th>
                                <th>Class Course</th>
                                <th>Class Lecturer</th>
                                <th>Semester</th>
                                <th>Action</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>{form.class_id}</td>
                                <td><input type="text" name="class_id" value={form.class_id} onChange={handleChange} disabled /></td>
                                <td><input type="text" name="class_number" value={form.class_number} onChange={handleChange} /></td>
                                <td><input type="text" name="class_course" value={form.class_course} onChange={handleChange} /></td>
                                <td><input type="text" name="class_lecturer" value={form.class_lecturer} onChange={handleChange} /></td>
                                <td><input type="text" name="class_semester" value={form.class_semester} onChange={handleChange} /></td>
                                <td>
                                    <button type="submit" className="btn btn-success">Update Class</button>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </form>
            </div>
        </Layout>
    );
};

export default ClassUpdate;

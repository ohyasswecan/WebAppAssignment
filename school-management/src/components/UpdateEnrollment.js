// src/components/UpdateEnrollment.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams, useNavigate } from 'react-router-dom';
import Layout from './Layout';

const UpdateEnrollment = () => {
    const { id } = useParams();
    const navigate = useNavigate();
    const [form, setForm] = useState({
        student_id: '',
        class_id: '',
        student_grade: '',
        enrollment_date: '',
        grade_date: '',
    });
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchEnrollment = async () => {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/api/student_enrollments/${id}/`);
                setForm({
                    student_id: response.data.student_id,
                    class_id: response.data.class_id,
                    student_grade: response.data.student_grade,
                    enrollment_date: response.data.enrollment_date,
                    grade_date: response.data.grade_date,
                });
                setLoading(false);
            } catch (error) {
                console.error('Error fetching enrollment:', error);
                setError(error);
                setLoading(false);
            }
        };

        fetchEnrollment();
    }, [id]);

    const handleChange = (e) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.put(`http://127.0.0.1:8000/api/student_enrollments/${id}/`, form);
            navigate('/student_enrollments');
        } catch (error) {
            console.error('Error updating enrollment:', error);
            setError(error);
        }
    };

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error loading enrollment: {error.message}</p>;

    return (
        <Layout>
            <div>
                <h1>Update Enrollment</h1>
                <form onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label>Student ID</label>
                        <input
                            type="text"
                            name="student_id"
                            value={form.student_id}
                            onChange={handleChange}
                            className="form-control"
                        />
                    </div>
                    <div className="form-group">
                        <label>Class ID</label>
                        <input
                            type="text"
                            name="class_id"
                            value={form.class_id}
                            onChange={handleChange}
                            className="form-control"
                        />
                    </div>
                    <div className="form-group">
                        <label>Grade</label>
                        <input
                            type="number"
                            name="student_grade"
                            value={form.student_grade}
                            onChange={handleChange}
                            className="form-control"
                        />
                    </div>
                    <div className="form-group">
                        <label>Enrollment Date</label>
                        <input
                            type="date"
                            name="enrollment_date"
                            value={form.enrollment_date}
                            onChange={handleChange}
                            className="form-control"
                        />
                    </div>
                    <div className="form-group">
                        <label>Grade Date</label>
                        <input
                            type="date"
                            name="grade_date"
                            value={form.grade_date}
                            onChange={handleChange}
                            className="form-control"
                        />
                    </div>
                    <button type="submit" className="btn btn-primary">Update Enrollment</button>
                </form>
            </div>
        </Layout>
    );
};

export default UpdateEnrollment;

// src/components/UpdateStudent.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams, useNavigate } from 'react-router-dom';
import Layout from './Layout';

const UpdateStudent = () => {
    const { studentId } = useParams();
    const [student, setStudent] = useState({
        student_id: '',
        student_firstname: '',
        student_lastname: '',
        student_email: '',
        student_DOB: '',
    });
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchStudent = async () => {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/api/students/${studentId}/`);
                setStudent(response.data);
                setLoading(false);
            } catch (error) {
                console.error('Error fetching student details:', error);
                setError(error);
                setLoading(false);
            }
        };

        fetchStudent();
    }, [studentId]);

    const handleChange = (e) => {
        setStudent({ ...student, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.put(`http://127.0.0.1:8000/api/students/${studentId}/`, student);
            navigate('/students');
        } catch (error) {
            console.error('Error updating student:', error);
            setError(error);
        }
    };

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error loading student details: {error.message}</p>;

    return (
        <Layout>
            <div>
                <h1>Update Student</h1>
                <form onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label htmlFor="student_firstname">First Name</label>
                        <input
                            type="text"
                            className="form-control"
                            id="student_firstname"
                            name="student_firstname"
                            value={student.student_firstname}
                            onChange={handleChange}
                        />
                    </div>
                    <div className="form-group">
                        <label htmlFor="student_lastname">Last Name</label>
                        <input
                            type="text"
                            className="form-control"
                            id="student_lastname"
                            name="student_lastname"
                            value={student.student_lastname}
                            onChange={handleChange}
                        />
                    </div>
                    <div className="form-group">
                        <label htmlFor="student_email">Email</label>
                        <input
                            type="email"
                            className="form-control"
                            id="student_email"
                            name="student_email"
                            value={student.student_email}
                            onChange={handleChange}
                        />
                    </div>
                    <div className="form-group">
                        <label htmlFor="student_DOB">Date of Birth</label>
                        <input
                            type="date"
                            className="form-control"
                            id="student_DOB"
                            name="student_DOB"
                            value={student.student_DOB}
                            onChange={handleChange}
                        />
                    </div>
                    <button type="submit" className="btn btn-primary">Update Student</button>
                </form>
            </div>
        </Layout>
    );
};

export default UpdateStudent;

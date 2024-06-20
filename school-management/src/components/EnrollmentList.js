// src/components/EnrollmentList.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import Layout from './Layout';

const EnrollmentList = () => {
    console.log("EnrollmentList component rendered"); // Debugging log

    const [enrollments, setEnrollments] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [form, setForm] = useState({
        student_id: '',
        class_id: '',
        enrollment_date: '',
        grade_date: '',
        student_grade: '',
    });
    const navigate = useNavigate();

    useEffect(() => {
        console.log("useEffect called"); // Debugging log
        const fetchEnrollments = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/student_enrollments/');
                console.log('Fetched enrollments:', response.data); // Debugging log
                setEnrollments(response.data);
                setLoading(false);
            } catch (error) {
                console.error('Error fetching enrollments:', error);
                setError(error);
                setLoading(false);
            }
        };

        fetchEnrollments();
    }, []);

    const handleChange = (e) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://127.0.0.1:8000/api/student_enrollments/', form);
            console.log('Added enrollment:', response.data); // Debugging log
            setEnrollments([...enrollments, response.data]);
        } catch (error) {
            console.error('Error adding enrollment:', error);
        }
    };

    const handleEdit = (enrollmentId) => {
        navigate(`/student_enrollments/update/${enrollmentId}`);
    };

    const handleDelete = async (enrollmentId) => {
        console.log('Deleting enrollment with ID:', enrollmentId); // Debugging log
        try {
            await axios.delete(`http://127.0.0.1:8000/api/student_enrollments/${enrollmentId}/`);
            setEnrollments(enrollments.filter(enrollment => enrollment.id !== enrollmentId));
        } catch (error) {
            console.error('Error deleting enrollment:', error);
            setError(error);
        }
    };

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error loading enrollments: {error.message}</p>;

    return (
        <Layout>
            <div>
                <h1>Enrollment List Page</h1>
                <form onSubmit={handleSubmit}>
                    <table className="table">
                        <thead>
                            <tr>
                                <th>#</th>
                                <th>Student ID</th>
                                <th>Class ID</th>
                                <th>Enrollment Date</th>
                                <th>Grade Date</th>
                                <th>Grade</th>
                                <th>Action</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>New</td>
                                <td><input type="text" name="student_id" value={form.student_id} onChange={handleChange} /></td>
                                <td><input type="text" name="class_id" value={form.class_id} onChange={handleChange} /></td>
                                <td><input type="date" name="enrollment_date" value={form.enrollment_date} onChange={handleChange} /></td>
                                <td><input type="date" name="grade_date" value={form.grade_date} onChange={handleChange} /></td>
                                <td><input type="text" name="student_grade" value={form.student_grade} onChange={handleChange} /></td>
                                <td>
                                    <button type="submit" className="btn btn-success">Add Enrollment</button>
                                </td>
                            </tr>
                            {enrollments.map((enrollment, index) => (
                                <tr key={enrollment.id}>
                                    <th scope="row">{index + 1}</th>
                                    <td>{enrollment.student_id}</td>
                                    <td>{enrollment.class_id}</td>
                                    <td>{enrollment.enrollment_date}</td>
                                    <td>{enrollment.grade_date}</td>
                                    <td>{enrollment.student_grade}</td>
                                    <td>
                                        <a href={`/student_enrollments/${enrollment.id}`} className="btn btn-primary btn-sm">Detail</a>
                                        <button
                                            onClick={() => handleEdit(enrollment.id)}
                                            className="btn btn-primary btn-sm"
                                        >
                                            Update
                                        </button>
                                        <button
                                            onClick={() => {
                                                if (window.confirm('Are you sure you want to delete this?')) {
                                                    handleDelete(enrollment.id);
                                                }
                                            }}
                                            className="btn btn-danger btn-sm"
                                        >
                                            Delete
                                        </button>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </form>
                <nav>
                    <ul className="pagination">
                        {/* Pagination logic here for future */}
                    </ul>
                </nav>
            </div>
        </Layout>
    );
};

export default EnrollmentList;

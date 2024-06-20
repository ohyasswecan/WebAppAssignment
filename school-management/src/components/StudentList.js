// src/components/StudentList.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import Layout from './Layout';

const StudentList = () => {
    const [students, setStudents] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [form, setForm] = useState({
        student_id: '',
        student_firstname: '',
        student_lastname: '',
        student_email: '',
        student_DOB: '',
    });
    const navigate = useNavigate();

    useEffect(() => {
        const fetchStudents = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/students/');
                setStudents(response.data);
                setLoading(false);
            } catch (error) {
                console.error('Error fetching students:', error);
                setError(error);
                setLoading(false);
            }
        };

        fetchStudents();
    }, []);

    const handleChange = (e) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        console.log('Form data to be submitted:', form); // Add this log to see form data
        try {
            const response = await axios.post('http://127.0.0.1:8000/api/students/', form);
            console.log('Added student:', response.data); // Add this log to see response data
            setStudents([...students, response.data]);
        } catch (error) {
            console.error('Error adding student:', error);
            setError(error);
        }
    };

    const handleEdit = (studentId) => {
        navigate(`/students/update/${studentId}`);
    };

    const handleDelete = async (studentId) => {
        console.log('Deleting student with ID:', studentId); // Add this log to see which ID is being deleted
        try {
            await axios.delete(`http://127.0.0.1:8000/api/students/${studentId}/`);
            setStudents(students.filter(student => student.student_id !== studentId));
        } catch (error) {
            console.error('Error deleting student:', error);
            setError(error);
        }
    };

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error: {error.message}</p>;

    return (
        <Layout>
            <div>
                <h1>Student List Page</h1>
                <a href="/upload_excel/">Excel Upload Student List</a>
                <form onSubmit={handleSubmit}>
                    <table className="table">
                        <thead>
                        <tr>
                            <th>#</th>
                            <th>Student ID</th>
                            <th>First Name</th>
                            <th>Last Name</th>
                            <th>Email</th>
                            <th>Date of Birth</th>
                            <th>Action</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td>New</td>
                            <td><input type="text" name="student_id" value={form.student_id} onChange={handleChange} /></td>
                            <td><input type="text" name="student_firstname" value={form.student_firstname} onChange={handleChange} /></td>
                            <td><input type="text" name="student_lastname" value={form.student_lastname} onChange={handleChange} /></td>
                            <td><input type="email" name="student_email" value={form.student_email} onChange={handleChange} /></td>
                            <td><input type="date" name="student_DOB" value={form.student_DOB} onChange={handleChange} /></td>
                            <td>
                                <button type="submit" className="btn btn-success">Add Student</button>
                            </td>
                        </tr>
                        {students.map((student, index) => (
                            <tr key={student.student_id}>
                                <th scope="row">{index + 1}</th>
                                <td>{student.student_id}</td>
                                <td>{student.student_firstname}</td>
                                <td>{student.student_lastname}</td>
                                <td>{student.student_email}</td>
                                <td>{student.student_DOB}</td>
                                <td>
                                    <a href={`/students/${student.student_id}`} className="btn btn-primary btn-sm">Detail</a>
                                    <button
                                        onClick={() => handleEdit(student.student_id)}
                                        className="btn btn-primary btn-sm"
                                    >
                                        Update
                                    </button>
                                    <button
                                        onClick={() => {
                                            if (window.confirm('Are you sure you want to delete this?')) {
                                                handleDelete(student.student_id);
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
                {/* Pagination if needed */}
                <nav>
                    <ul className="pagination">
                        {/* Pagination logic here for future */}
                    </ul>
                </nav>
            </div>
        </Layout>
    );
};

export default StudentList;

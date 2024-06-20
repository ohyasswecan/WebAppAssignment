// src/components/LecturerList.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Layout from './Layout';

const LecturerList = () => {
    const [lecturers, setLecturers] = useState([]);
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
        const fetchLecturers = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/lecturers/');
                setLecturers(response.data);
                setLoading(false);
            } catch (error) {
                console.error('Error fetching lecturers:', error);
                setError(error);
                setLoading(false);
            }
        };

        fetchLecturers();
    }, []);

    const handleChange = (e) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://127.0.0.1:8000/api/lecturers/', form);
            setLecturers([...lecturers, response.data]);
            setForm({
                staff_id: '',
                lecturer_firstname: '',
                lecturer_lastname: '',
                lecturer_email: '',
                lecturer_DOB: '',
            });
        } catch (error) {
            console.error('Error adding lecturer:', error);
        }
    };

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error loading lecturers: {error.message}</p>;

    return (
        <Layout>
            <div>
                <h1>Lecturer List Page</h1>
                <form onSubmit={handleSubmit}>
                    <table className="table">
                        <thead>
                            <tr>
                                <th>#</th>
                                <th>Staff ID</th>
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
                                <td><input type="text" name="staff_id" value={form.staff_id} onChange={handleChange} /></td>
                                <td><input type="text" name="lecturer_firstname" value={form.lecturer_firstname} onChange={handleChange} /></td>
                                <td><input type="text" name="lecturer_lastname" value={form.lecturer_lastname} onChange={handleChange} /></td>
                                <td><input type="email" name="lecturer_email" value={form.lecturer_email} onChange={handleChange} /></td>
                                <td><input type="date" name="lecturer_DOB" value={form.lecturer_DOB} onChange={handleChange} /></td>
                                <td>
                                    <button type="submit" className="btn btn-success">Add Lecturer</button>
                                </td>
                            </tr>
                            {lecturers.map((lecturer, index) => (
                                <tr key={lecturer.staff_id}>
                                    <th scope="row">{index + 1}</th>
                                    <td>{lecturer.staff_id}</td>
                                    <td>{lecturer.lecturer_firstname}</td>
                                    <td>{lecturer.lecturer_lastname}</td>
                                    <td>{lecturer.lecturer_email}</td>
                                    <td>{lecturer.lecturer_DOB}</td>
                                    <td>
                                        <a href={`/lecturers/${lecturer.staff_id}`} className="btn btn-primary btn-sm">Detail</a>
                                        <a href={`/lecturers/update/${lecturer.staff_id}`} className="btn btn-primary btn-sm">Update</a>
                                        <a href={`/lecturers/delete/${lecturer.staff_id}`} className="btn btn-danger btn-sm" onClick={() => window.confirm('Are you sure you want to delete this?')}>Delete</a>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </form>
                {/* Pagination if needed */}
                <nav>
                    <ul className="pagination">
                        {/* Pagination logic here if using pagination */}
                    </ul>
                </nav>
            </div>
        </Layout>
    );
};

export default LecturerList;

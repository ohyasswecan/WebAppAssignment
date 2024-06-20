// src/components/SemesterList.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Layout from './Layout';

const SemesterList = () => {
    const [semesters, setSemesters] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [form, setForm] = useState({
        semester_id: '',
        semester_name: '',
        semester_year: '',
    });

    useEffect(() => {
        const fetchSemesters = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/semesters/');
                setSemesters(response.data);
                setLoading(false);
            } catch (error) {
                console.error('Error fetching semesters:', error);
                setError(error);
                setLoading(false);
            }
        };

        fetchSemesters();
    }, []);

    const handleChange = (e) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://127.0.0.1:8000/api/semesters/', form);
            setSemesters([...semesters, response.data]);
        } catch (error) {
            console.error('Error adding semester:', error);
        }
    };

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error loading semesters: {error.message}</p>;

    return (
        <Layout>
            <div>
                <h1>Semester List Page</h1>
                <form onSubmit={handleSubmit}>
                    <table className="table">
                        <thead>
                            <tr>
                                <th>#</th>
                                <th>Semester ID</th>
                                <th>Semester Name</th>
                                <th>Semester Year</th>
                                <th>Action</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>New</td>
                                <td><input type="text" name="semester_id" value={form.semester_id} onChange={handleChange} /></td>
                                <td><input type="text" name="semester_name" value={form.semester_name} onChange={handleChange} /></td>
                                <td><input type="text" name="semester_year" value={form.semester_year} onChange={handleChange} /></td>
                                <td>
                                    <button type="submit" className="btn btn-success">Add Semester</button>
                                </td>
                            </tr>
                            {semesters.map((semester, index) => (
                                <tr key={semester.semester_id}>
                                    <th scope="row">{index + 1}</th>
                                    <td>{semester.semester_id}</td>
                                    <td>{semester.semester_name}</td>
                                    <td>{semester.semester_year}</td>
                                    <td>
                                        <a href={`/semesters/${semester.semester_id}`} className="btn btn-primary btn-sm">Detail</a>
                                        <a href={`/semesters/update/${semester.semester_id}`} className="btn btn-primary btn-sm">Update</a>
                                        <a href={`/semesters/delete/${semester.semester_id}`} className="btn btn-danger btn-sm"
                                           onClick={() => window.confirm('Are you sure you want to delete this?')}>Delete</a>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </form>
                <nav>
                    <ul className="pagination">
                        {/* Pagination logic here if using pagination */}
                    </ul>
                </nav>
            </div>
        </Layout>
    );
};

export default SemesterList;

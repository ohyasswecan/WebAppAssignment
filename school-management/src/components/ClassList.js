// src/components/ClassList.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Layout from './Layout';

const ClassList = () => {
    const [classes, setClasses] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [form, setForm] = useState({
        class_id: '',
        class_number: '',
        class_course: '',
        class_lecturer: '',
        class_semester: '',
    });

    useEffect(() => {
        const fetchClasses = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/class_enrollments/');
                setClasses(response.data);
                setLoading(false);
            } catch (error) {
                console.error('Error fetching classes:', error);
                setError(error);
                setLoading(false);
            }
        };

        fetchClasses();
    }, []);

    const handleChange = (e) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://127.0.0.1:8000/api/class_enrollments/', form);
            setClasses([...classes, response.data]);
        } catch (error) {
            console.error('Error adding class:', error);
        }
    };

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error loading classes: {error.message}</p>;

    return (
        <Layout>
            <div>
                <h1>Class List Page</h1>
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
                                <td>New</td>
                                <td><input type="text" name="class_id" value={form.class_id} onChange={handleChange} /></td>
                                <td><input type="text" name="class_number" value={form.class_number} onChange={handleChange} /></td>
                                <td><input type="text" name="class_course" value={form.class_course} onChange={handleChange} /></td>
                                <td><input type="text" name="class_lecturer" value={form.class_lecturer} onChange={handleChange} /></td>
                                <td><input type="text" name="class_semester" value={form.class_semester} onChange={handleChange} /></td>
                                <td>
                                    <button type="submit" className="btn btn-success">Add Class</button>
                                </td>
                            </tr>
                            {classes.map((classItem, index) => (
                                <tr key={classItem.class_id}>
                                    <th scope="row">{index + 1}</th>
                                    <td>{classItem.class_id}</td>
                                    <td>{classItem.class_number}</td>
                                    <td>{classItem.class_course}</td>
                                    <td>{classItem.class_lecturer}</td>
                                    <td>{classItem.class_semester}</td>
                                    <td>
                                        <a href={`/class_enrollments/${classItem.class_id}`} className="btn btn-primary btn-sm">Detail</a>
                                        <a href={`/class_enrollments/update/${classItem.class_id}`} className="btn btn-primary btn-sm">Update</a>
                                        <a href={`/class_enrollments/delete/${classItem.class_id}`} className="btn btn-danger btn-sm"
                                           onClick={() => window.confirm('Are you sure you want to delete this?')}>Delete</a>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </form>
                {/* Pagination if needed */}
                <nav>
                    <ul className="pagination">
                    </ul>
                </nav>
            </div>
        </Layout>
    );
};

export default ClassList;

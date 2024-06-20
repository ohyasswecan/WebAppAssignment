// src/components/CourseList.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import Layout from './Layout';

const CourseList = () => {
    const [courses, setCourses] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [form, setForm] = useState({
        course_id: '',
        course_code: '',
        course_name: '',
    });
    const navigate = useNavigate();

    useEffect(() => {
        const fetchCourses = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/courses/');
                setCourses(response.data);
                setLoading(false);
            } catch (error) {
                console.error('Error fetching courses:', error);
                setError(error);
                setLoading(false);
            }
        };

        fetchCourses();
    }, []);

    const handleChange = (e) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://127.0.0.1:8000/api/courses/', form);
            setCourses([...courses, response.data]);
        } catch (error) {
            console.error('Error adding course:', error);
        }
    };

    const handleDelete = async (courseId) => {
        if (window.confirm('Are you sure you want to delete this?')) {
            try {
                await axios.delete(`http://127.0.0.1:8000/api/courses/${courseId}/`);
                setCourses(courses.filter(course => course.course_id !== courseId));
            } catch (error) {
                console.error('Error deleting course:', error);
            }
        }
    };

    const handleUpdate = (courseId) => {
        navigate(`/courses/update/${courseId}`);
    };

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error loading courses: {error.message}</p>;

    return (
        <Layout>
            <div>
                <h1>Course List Page</h1>
                <form onSubmit={handleSubmit}>
                    <table className="table">
                        <thead>
                            <tr>
                                <th>#</th>
                                <th>Course ID</th>
                                <th>Course Code</th>
                                <th>Course Name</th>
                                <th>Action</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>New</td>
                                <td><input type="text" name="course_id" value={form.course_id} onChange={handleChange} /></td>
                                <td><input type="text" name="course_code" value={form.course_code} onChange={handleChange} /></td>
                                <td><input type="text" name="course_name" value={form.course_name} onChange={handleChange} /></td>
                                <td>
                                    <button type="submit" className="btn btn-success">Add Course</button>
                                </td>
                            </tr>
                            {courses.map((course, index) => (
                                <tr key={course.course_id}>
                                    <th scope="row">{index + 1}</th>
                                    <td>{course.course_id}</td>
                                    <td>{course.course_code}</td>
                                    <td>{course.course_name}</td>
                                    <td>
                                        <a href={`/courses/${course.course_id}`} className="btn btn-primary btn-sm">Detail</a>
                                        <button onClick={() => handleUpdate(course.course_id)} className="btn btn-primary btn-sm">Update</button>
                                        <button onClick={() => handleDelete(course.course_id)} className="btn btn-danger btn-sm">Delete</button>
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

export default CourseList;

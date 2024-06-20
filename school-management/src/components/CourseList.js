// src/components/CourseList.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';
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
                                        <a href={`/courses/update/${course.course_id}`} className="btn btn-primary btn-sm">Update</a>
                                        <a href={`/courses/delete/${course.course_id}`} className="btn btn-danger btn-sm"
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

export default CourseList;

// src/components/UpdateCourse.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams, useNavigate } from 'react-router-dom';
import Layout from './Layout';

const CourseUpdate = () => {
    const { courseId } = useParams();
    const [course, setCourse] = useState({
        course_id: '',
        course_code: '',
        course_name: ''
    });
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchCourse = async () => {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/api/courses/${courseId}/`);
                setCourse(response.data);
                setLoading(false);
            } catch (error) {
                console.error('Error fetching course:', error);
                setError(error);
                setLoading(false);
            }
        };

        fetchCourse();
    }, [courseId]);

    const handleChange = (e) => {
        setCourse({ ...course, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.put(`http://127.0.0.1:8000/api/courses/${courseId}/`, course);
            navigate('/courses');
        } catch (error) {
            console.error('Error updating course:', error);
            setError(error);
        }
    };

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error loading course: {error.message}</p>;

    return (
        <Layout>
            <div>
                <h1>Update Course</h1>
                <form onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label htmlFor="course_id">Course ID</label>
                        <input
                            type="text"
                            className="form-control"
                            id="course_id"
                            name="course_id"
                            value={course.course_id}
                            onChange={handleChange}
                            disabled
                        />
                    </div>
                    <div className="form-group">
                        <label htmlFor="course_code">Course Code</label>
                        <input
                            type="text"
                            className="form-control"
                            id="course_code"
                            name="course_code"
                            value={course.course_code}
                            onChange={handleChange}
                        />
                    </div>
                    <div className="form-group">
                        <label htmlFor="course_name">Course Name</label>
                        <input
                            type="text"
                            className="form-control"
                            id="course_name"
                            name="course_name"
                            value={course.course_name}
                            onChange={handleChange}
                        />
                    </div>
                    <button type="submit" className="btn btn-primary">Update Course</button>
                </form>
            </div>
        </Layout>
    );
};

export default CourseUpdate;

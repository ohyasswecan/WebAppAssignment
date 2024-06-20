// src/components/CourseDetail.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import Layout from './Layout';

const CourseDetail = () => {
    const { courseId } = useParams();
    const [course, setCourse] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchCourse = async () => {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/api/courses/${courseId}/`);
                setCourse(response.data);
                setLoading(false);
            } catch (error) {
                console.error('Error fetching course details:', error);
                setError(error);
                setLoading(false);
            }
        };

        fetchCourse();
    }, [courseId]);

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error loading course details: {error.message}</p>;

    return (
        <Layout>
            <div>
                <h1>Course Detail Page</h1>
                {course && (
                    <div>
                        <p>Course ID: {course.course_id}</p>
                        <p>Course Code: {course.course_code}</p>
                        <p>Course Name: {course.course_name}</p>
                    </div>
                )}
            </div>
        </Layout>
    );
};

export default CourseDetail;

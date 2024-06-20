// src/components/EnrollmentDetail.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import Layout from './Layout';

const EnrollmentDetail = () => {
    const { id } = useParams();
    const [enrollment, setEnrollment] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchEnrollment = async () => {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/api/student_enrollments/${id}/`);
                setEnrollment(response.data);
                setLoading(false);
            } catch (error) {
                console.error('Error fetching enrollment details:', error);
                setError(error);
                setLoading(false);
            }
        };

        fetchEnrollment();
    }, [id]);

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error loading enrollment details: {error.message}</p>;

    return (
        <Layout>
            <div>
                <h1>Enrollment Detail</h1>
                {enrollment && (
                    <div>
                        <p>Student ID: {enrollment.student_id}</p>
                        <p>Class ID: {enrollment.class_id}</p>
                        <p>Enrollment Date: {enrollment.enrollment_date}</p>
                        <p>Grade Date: {enrollment.grade_date}</p>
                        <p>Grade: {enrollment.student_grade}</p>
                    </div>
                )}
            </div>
        </Layout>
    );
};

export default EnrollmentDetail;

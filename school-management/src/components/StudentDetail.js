// src/components/StudentDetail.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import Layout from "./Layout";

const StudentDetail = () => {
    const { studentId } = useParams();
    const [student, setStudent] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchStudent = async () => {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/api/students/${studentId}/`);
                setStudent(response.data);
                setLoading(false);
            } catch (error) {
                console.error('Error fetching student details:', error);
                setError(error);
                setLoading(false);
            }
        };

        fetchStudent();
    }, [studentId]);

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error loading student details: {error.message}</p>;

    return (
        <Layout>
            <div>
                <h1>Student Detail</h1>
                {student && (
                    <div>
                        <p>Student ID: {student.student_id}</p>
                        <p>First Name: {student.student_firstname}</p>
                        <p>Last Name: {student.student_lastname}</p>
                        <p>Email: {student.student_email}</p>
                        <p>Date of Birth: {student.student_DOB}</p>
                    </div>
                )}
            </div>
        </Layout>

    );
};

export default StudentDetail;

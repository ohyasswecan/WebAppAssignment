// src/components/ClassDetail.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import Layout from './Layout';

const ClassDetail = () => {
    const { classId } = useParams();
    const [classItem, setClassItem] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchClassItem = async () => {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/api/class_enrollments/${classId}/`);
                setClassItem(response.data);
                setLoading(false);
            } catch (error) {
                console.error('Error fetching class details:', error);
                setError(error);
                setLoading(false);
            }
        };

        fetchClassItem();
    }, [classId]);

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error loading class details: {error.message}</p>;

    return (
        <Layout>
            <div>
                <h1>Class Detail</h1>
                {classItem && (
                    <div>
                        <p>Class ID: {classItem.class_id}</p>
                        <p>Class Number: {classItem.class_number}</p>
                        <p>Class Course: {classItem.class_course}</p>
                        <p>Class Lecturer: {classItem.class_lecturer}</p>
                        <p>Semester: {classItem.class_semester}</p>
                    </div>
                )}
            </div>
        </Layout>
    );
};

export default ClassDetail;

// src/components/SemesterDetail.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import Layout from './Layout';

const SemesterDetail = () => {
    const { semesterId } = useParams();
    const [semester, setSemester] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchSemester = async () => {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/api/semesters/${semesterId}/`);
                setSemester(response.data);
                setLoading(false);
            } catch (error) {
                console.error('Error fetching semester details:', error);
                setError(error);
                setLoading(false);
            }
        };

        fetchSemester();
    }, [semesterId]);

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error loading semester details: {error.message}</p>;

    return (
        <Layout>
            <div>
                <h1>Semester Detail Page</h1>
                {semester && (
                    <div>
                        <p>Semester ID: {semester.semester_id}</p>
                        <p>Semester Name: {semester.semester_name}</p>
                        <p>Semester Year: {semester.semester_year}</p>
                    </div>
                )}
            </div>
        </Layout>
    );
};

export default SemesterDetail;

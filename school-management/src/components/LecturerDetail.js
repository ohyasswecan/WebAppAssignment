import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import Layout from './Layout';

const LecturerDetail = () => {
    const { lecturerId } = useParams();
    const [lecturer, setLecturer] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchLecturer = async () => {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/api/lecturers/${lecturerId}/`);
                setLecturer(response.data);
                setLoading(false);
            } catch (error) {
                console.error('Error fetching lecturer details:', error);
                setError(error);
                setLoading(false);
            }
        };

        fetchLecturer();
    }, [lecturerId]);

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error loading lecturer details: {error.message}</p>;

    return (
        <Layout>
            <div>
                <h1>Lecturer Detail Page</h1>
                {lecturer && (
                    <table>
                        <tr>
                            <th>Staff ID</th>
                            <td>{lecturer.staff_id}</td>
                        </tr>
                        <tr>
                            <th>Lecturer First Name</th>
                            <td>{lecturer.lecturer_firstname}</td>
                        </tr>
                        <tr>
                            <th>Lecturer Last Name</th>
                            <td>{lecturer.lecturer_lastname}</td>
                        </tr>
                        <tr>
                            <th>Lecturer Email</th>
                            <td>{lecturer.lecturer_email}</td>
                        </tr>
                        <tr>
                            <th>Lecturer Course</th>
                            <td>{lecturer.lecturer_course}</td>
                        </tr>
                        <tr>
                            <th>Lecturer Date of Birth</th>
                            <td>{lecturer.lecturer_DOB}</td>
                        </tr>
                    </table>
                )}
            </div>
        </Layout>
    );
};

export default LecturerDetail;

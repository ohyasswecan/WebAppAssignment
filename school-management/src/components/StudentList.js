import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Layout from "./Layout";

const StudentList = () => {
    const [students, setStudents] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchStudents = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/students/');
                setStudents(response.data);
                setLoading(false);
            } catch (error) {
                console.error('Error fetching students:', error);
                setError(error);
                setLoading(false);
            }
        };

        fetchStudents();
    }, []);

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error loading students: {error.message}</p>;

    return (
        <Layout>
            <div>
                <h1>Student List Page</h1>
                <a href="/StudentList/UploadStudentList">Excel Upload Student List</a>
                <form method="POST" action="/StudentList/CreateStudent/">
                    <table className="table">
                        <thead>
                        <tr>
                            <th>#</th>
                            <th>Student ID</th>
                            <th>First Name</th>
                            <th>Last Name</th>
                            <th>Email</th>
                            <th>Date of Birth</th>
                            <th>Action</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td>New</td>
                            <td><input type="text" name="student_id"/></td>
                            <td><input type="text" name="student_firstname"/></td>
                            <td><input type="text" name="student_lastname"/></td>
                            <td><input type="email" name="student_email"/></td>
                            <td><input type="date" name="student_DOB"/></td>
                            <td>
                                <button type="submit" className="btn btn-success">Add Student</button>
                            </td>
                        </tr>
                        {students.map((student, index) => (
                            <tr key={student.student_id}>
                                <th scope="row">{index + 1}</th>
                                <td>{student.student_id}</td>
                                <td>{student.student_firstname}</td>
                                <td>{student.student_lastname}</td>
                                <td>{student.student_email}</td>
                                <td>{student.student_DOB}</td>
                                <td>
                                    <a href={`/students/${student.student_id}`}
                                       className="btn btn-primary btn-sm">Detail</a>
                                    <a href={`/StudentList/StudentDetail/UpdateStudent/${student.student_id}`}
                                       className="btn btn-primary btn-sm">Update</a>
                                    <a href={`/StudentList/StudentDetail/DeleteStudent/${student.student_id}`}
                                       className="btn btn-danger btn-sm"
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
                        {/* Pagination logic here if using pagination */}
                    </ul>
                </nav>
            </div>
        </Layout>

    );
};

export default StudentList;

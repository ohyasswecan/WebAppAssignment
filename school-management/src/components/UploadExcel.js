import React, { useState } from 'react';
import axios from 'axios';
import * as XLSX from 'xlsx';
import Layout from './Layout';

const UploadExcel = () => {
    const [file, setFile] = useState(null);
    const [data, setData] = useState([]);
    const [error, setError] = useState(null);
    const [showInsertForm, setShowInsertForm] = useState(false);

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleUpload = (e) => {
        e.preventDefault();
        if (file) {
            const reader = new FileReader();
            reader.onload = (event) => {
                const bstr = event.target.result;
                const wb = XLSX.read(bstr, { type: 'binary' });
                const wsname = wb.SheetNames[0];
                const ws = wb.Sheets[wsname];
                const jsonData = XLSX.utils.sheet_to_json(ws);
                setData(jsonData);
                setShowInsertForm(true);
            };
            reader.readAsBinaryString(file);
        } else {
            setError({ message: 'No file selected' });
        }
    };

    const handleInsert = async () => {
        try {
            const response = await axios.post('http://127.0.0.1:8000/app/api/insert_list/', data, {
                headers: {
                    'Content-Type': 'application/json',
                },
            });
            alert('Data inserted successfully');
            setData([]);
            setShowInsertForm(false);
        } catch (error) {
            console.error('Error inserting data:', error);
            setError(error);
        }
    };

    return (
        <Layout>
            <div>
                <h1>Upload Excel File</h1>
                <form onSubmit={handleUpload}>
                    <input type="file" onChange={handleFileChange} />
                    <button type="submit" className="btn btn-success">Upload</button>
                </form>

                {error && <p>Error: {error.message}</p>}

                {showInsertForm && (
                    <div>
                        <h2>Data from Excel File</h2>
                        <table className="table table-striped">
                            <thead>
                                <tr>
                                    <th>Student ID</th>
                                    <th>First Name</th>
                                    <th>Last Name</th>
                                    <th>Email</th>
                                    <th>Date of Birth</th>
                                </tr>
                            </thead>
                            <tbody>
                                {data.map((row, index) => (
                                    <tr key={index}>
                                        <td>{row.student_id}</td>
                                        <td>{row.student_firstname}</td>
                                        <td>{row.student_lastname}</td>
                                        <td>{row.student_email}</td>
                                        <td>{row.student_DOB}</td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                        <button onClick={handleInsert} className="btn btn-primary">Insert Data</button>
                    </div>
                )}
            </div>
        </Layout>
    );
};

export default UploadExcel;

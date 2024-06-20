// src/index.js

import React from 'react';
import ReactDOM from 'react-dom/client'; // Update this import
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import App from './App';
import StudentList from './components/StudentList';
import StudentDetail from './components/StudentDetail';
import 'bootstrap/dist/css/bootstrap.min.css';
import ClassList from './components/ClassList';
import ClassDetail from './components/ClassDetail';
import LecturerList from "./components/LecturerList";
import LecturerDetail from "./components/LecturerDetail";
import CourseList from "./components/CourseList";
import CourseDetail from "./components/CourseDetail";
import SemesterList from "./components/SemesterList";
import SemesterDetail from "./components/SemesterDetail";
import EnrollmentList from "./components/EnrollmentList";
import EnrollmentDetail from "./components/EnrollmentDetail";

const root = ReactDOM.createRoot(document.getElementById('root')); // Use createRoot
root.render(
    <Router>
        <Routes>
            <Route path="*" element={<App/>}/>
            <Route path="/students" element={<StudentList/>}/>
            <Route path="/students/:studentId" element={<StudentDetail/>}/>
            <Route path="/class_enrollments" element={<ClassList/>}/>
            <Route path="/class_enrollments/:classId" element={<ClassDetail/>}/>
            <Route path="/lecturers" element={<LecturerList/>}/>
            <Route path="/lecturers/:lecturerId" element={<LecturerDetail/>}/>
            <Route path="/courses" element={<CourseList/>}/>
            <Route path="/courses/:courseId" element={<CourseDetail/>}/>
            <Route path="/semesters" element={<SemesterList/>}/>
            <Route path="/semesters/:semesterId" element={<SemesterDetail/>}/>
            <Route path="/student_enrollments" element={<EnrollmentList/>}/>
            <Route path="/student_enrollments/:id" element={<EnrollmentDetail/>}/>
            {/* Add other routes here */}
        </Routes>
    </Router>
);

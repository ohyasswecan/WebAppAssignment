// src/App.js

import React from 'react';
import {Routes, Route} from 'react-router-dom';
import Layout from './components/Layout';
import Home from './components/Home';
import StudentList from './components/StudentList';
import StudentDetail from './components/StudentDetail';
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
import ClassUpdate from "./components/ClassUpdate";
import CourseUpdate from "./components/CourseUpdate";
import UpdateSemester from "./components/UpdateSemester";
import UpdateStudent from "./components/UpdateStudent";
import UpdateLecturer from "./components/UpdateLecturer";
import UpdateEnrollment from "./components/UpdateEnrollment";
import UploadExcel from "./components/UploadExcel";
import LoginForm from "./components/Login";

function App() {
    return (
        <Layout>
            <Routes>
                  <Route path="/login" element={<LoginForm />} />
                <Route path="/" element={<Home/>}/>
                <Route path="/students" element={<StudentList/>}/>
                <Route path="/students/:studentId" element={<StudentDetail/>}/>
                <Route path="/students/update/:studentId" element={<UpdateStudent/>}/>
                <Route path="/class_enrollments" element={<ClassList/>}/>
                <Route path="/class_enrollments/:classId" element={<ClassDetail/>}/>
                <Route path="/class_enrollments/update/:classId" element={<ClassUpdate/>}/>
                <Route path="/lecturers" element={<LecturerList/>}/>
                <Route path="/lecturers/:lecturerId" element={<LecturerDetail/>}/>
                <Route path="/lecturers/update/:lecturerId" element={<UpdateLecturer/>}/>
                <Route path="/courses" element={<CourseList/>}/>
                <Route path="/courses/:courseId" element={<CourseDetail/>}/>
                <Route path="/courses/update/:courseId" element={<CourseUpdate/>}/>
                <Route path="/semesters" element={<SemesterList/>}/>
                <Route path="/semesters/:semesterId" element={<SemesterDetail/>}/>
                <Route path="/semesters/update/:semesterId" element={<UpdateSemester/>}/>
                <Route path="/student_enrollments" element={<EnrollmentList/>}/>
                <Route path="/student_enrollments/:id" element={<EnrollmentDetail/>}/>
                <Route path="/student_enrollments/update/:id" element={<UpdateEnrollment/>}/>
                <Route path="/upload_excel" element={<UploadExcel/>}/>
                {/* Add other routes here */}
            </Routes>
        </Layout>
    );
}

export default App;

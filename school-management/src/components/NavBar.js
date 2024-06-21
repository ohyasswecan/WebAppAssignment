// src/components/NavBar.js
import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap-icons/font/bootstrap-icons.css';
import UserContext from '../contexts/UserContext';

const NavBar = () => {
    const { user, logout } = useContext(UserContext);

    return (
        <nav className="navbar navbar-expand-md navbar-dark bg-dark mb-4">
            <div className="container-fluid">
                <Link className="navbar-brand" to="/">
                    <i className="bi bi-window-sidebar"></i> Grade Book System
                </Link>
                <button
                    className="navbar-toggler"
                    type="button"
                    data-bs-toggle="collapse"
                    data-bs-target="#navbarCollapse"
                    aria-controls="navbarCollapse"
                    aria-expanded="false"
                    aria-label="Toggle navigation"
                >
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarCollapse">
                    <ul className="navbar-nav me-auto mb-2 mb-md-0">
                        <li className="nav-item">
                            <Link className="nav-link active" aria-current="page" to="/">Home</Link>
                        </li>
                        <li className="nav-item">
                            <Link className="nav-link link-light" to="/class_enrollments">CLASS</Link>
                        </li>
                        <li className="nav-item">
                            <Link className="nav-link link-light" to="/courses">COURSE</Link>
                        </li>
                        <li className="nav-item">
                            <Link className="nav-link link-light" to="/semesters">SEMESTER</Link>
                        </li>
                        <li className="nav-item">
                            <Link className="nav-link link-light" to="/students">STUDENT</Link>
                        </li>
                        <li className="nav-item">
                            <Link className="nav-link link-light" to="/lecturers">LECTURER</Link>
                        </li>
                        <li className="nav-item">
                            <Link className="nav-link link-light" to="/student_enrollments">ENROLLMENT</Link>
                        </li>
                        {user ? (
                            <>
                                <li className="nav-item">
                                    <span className="navbar-text">
                                        <strong>{user.username}</strong>
                                    </span>
                                </li>
                                <li className="nav-item">
                                    <Link to="/update_userprofile">
                                        <img
                                            src={user.avatar}
                                            alt="User Avatar"
                                            style={{ width: "25px", height: "25px", objectFit: "cover" }}
                                        />
                                    </Link>
                                </li>
                                <li>
                                    <p className="text-light">Role: {user.role}</p>
                                </li>
                                <li className="nav-item">
                                    <button type="button" className="btn btn-outline-danger" onClick={logout}>Logout</button>
                                </li>
                            </>
                        ) : (
                            <>
                                <li className="nav-item">
                                    <Link className="nav-link link-light" to="/login">LOGIN</Link>
                                </li>
                                <li className="nav-item">
                                    <Link className="nav-link link-light" to="/register">REGISTER</Link>
                                </li>
                            </>
                        )}
                    </ul>
                    <form className="d-flex" role="search">
                        <input className="form-control me-2" type="search" placeholder="Search" aria-label="Search" />
                        <button className="btn btn-outline-success" type="submit">Search</button>
                    </form>
                </div>
            </div>
        </nav>
    );
};

export default NavBar;

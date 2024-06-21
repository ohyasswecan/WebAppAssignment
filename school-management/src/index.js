// src/index.js

import React from 'react';
import ReactDOM from 'react-dom/client'; // Update this import
import {BrowserRouter as Router} from 'react-router-dom';
import App from './App';
import 'bootstrap/dist/css/bootstrap.min.css';
import {UserProvider} from "./contexts/UserContext";

const root = ReactDOM.createRoot(document.getElementById('root')); // Use createRoot


root.render(
     <UserProvider>
        <Router>
            <App />
        </Router>
    </UserProvider>
);

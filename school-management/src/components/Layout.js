// src/components/Layout.js
import React from 'react';
import NavBar from './NavBar';

const Layout = ({ children }) => {
  return (
    <div>
      <NavBar />
      <div className="container">
        {children}
      </div>
    </div>
  );
};

export default Layout;

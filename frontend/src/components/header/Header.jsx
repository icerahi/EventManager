import React from "react";
import useAuth from "../../hooks/useAuth";
import SideBar from "../sideBar/SideBar";
import "./Header.css";
import {Link} from 'react-router-dom'
const Header = () => {
  const { user, setUser } = useAuth();

  const LogOut = () => {
    setUser(null);
    localStorage.removeItem("token");
  };

  return (
    <header className="sticky-top bg-white ">
      <nav className="container d-flex my-2 justify-content-between align-items-center">
        <h2>
         <Link className="text-decoration-none text-dark" to="/"> Task <span className="bg-warning p-1 rounded-3">Manager</span></Link>
        </h2>
        <div className="d-flex">
            {user?<a onClick={LogOut} style={{cursor:'pointer'}} className="text-decoration-underline h5 text-dark pe-auto border-0">
            {user?.username}(Logout)
          </a>:<Link to="/login"  className="text-decoration-underline h5 text-dark border-0">
            Login/Register
          </Link>}
          
        </div>
      </nav>
    </header>
  );
};

export default Header;

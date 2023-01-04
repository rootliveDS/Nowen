import React from 'react';
import './Header.css';


class Header extends React.Component {
  render() {
    return (
        <div className="header_head">
          <img className='header_logo' src='logo512.png' alt="Logo" />
          <p className='header_name'>Nowen</p>
            <div className='header_button'>
              <button onClick={(e) => {
                  e.preventDefault();
                  window.location.href='http://localhost:8000/login/';
                  }}className='header_button1'>Login</button>
              <button onClick={(e) => {
                  e.preventDefault();
                  window.location.href='http://localhost:8000/signup/';
                  }} className='header_button2'>Register</button>
            </div>
        </div>
        )
  }
}


export default Header;
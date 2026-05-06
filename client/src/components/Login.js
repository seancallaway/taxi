import React from 'react';
import { Link } from 'react-router-dom';

function Login (props) {
  return (
    <>
      <Link to='/'>Home</Link>
      <h1>Login</h1>
      <p>
        Don't have an account? <Link to='/sign-up'>Sign up here</Link>.
      </p>
    </>
  );
}

export default Login;

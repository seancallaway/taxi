import React from 'react';
import { Link } from 'react-router-dom';

function Landing (props) {
  return (
    <div>
      <h1>Taxi</h1>
      <Link to='/sign-up'>Sign Up</Link>
      <Link to='/login'>Login</Link>
    </div>
  );
}

export default Landing;

import React from 'react'
import { useState } from 'react';

const NameForm = () => {
    const [name, setName] = useState('');
    const [submittedName, setSubmittedName] = useState('');
  
    const handleChange = (event) => {
      setName(event.target.value);
    };
  
    const handleSubmit = (event) => {
      event.preventDefault();
      setSubmittedName(name);
      setName(''); // Clear the input field after submission
    };
  
    return (
      <div>
        <h3>Welcome to the greetings component (App)</h3>
        <h2>Enter Your Name</h2>
        <form onSubmit={handleSubmit}>
          <label>
            Name:
            <input type="text" value={name} onChange={handleChange} />
          </label>
          <button type="submit">Submit</button>
        </form>
  
        {submittedName && (
          <div>
            <h2>Greetings</h2>
            <p>Hello, {submittedName}!</p>
          </div>
        )}
      </div>
    );
  };

export default NameForm
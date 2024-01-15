// ParentComponent.jsx
import React from 'react';
import ChildComponent from './ChildComponent'; // Assuming the file is in the same directory

const ParentComponent =()=> {
  const messageFromParent = "Hello child...Message from the parent component, passed as props in this child component";

  return (
    <div className='parent'>
      <h1>Parent Component</h1>
      <ChildComponent message={messageFromParent} />
    </div>
  );
};

export default ParentComponent;

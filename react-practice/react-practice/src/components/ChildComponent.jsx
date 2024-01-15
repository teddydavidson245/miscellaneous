import React from "react";

const ChildComponent =(props)=> {
    const {message} = props;

    return (
        <div>
            <p>{message}</p>
        </div>
    );
};

export default ChildComponent;
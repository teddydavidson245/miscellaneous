import { useState, useEffect } from 'react';


function Count() {

  const [count, setCount] = useState(0)
  useEffect( ()=>{
    // the function is called when the component mounts
    document.title = "Hello React";
// Optionally, you can return a cleanup function to perform actions when the component unmounts

    return ()=> {
      document.title = "Unmounted component";
    }
  }, [] );

  return (
    <>

<h2>Count Component</h2>
<div>
<p> You have said "Hello world!" {count} times</p> 
 <button onClick={()=>setCount(count +1)}>Shout</button>
</div>
    </>
  )
}

export default Count;

import React, {useState, useEffect} from "react";

const TodoList = ()=>{
    const [task, setTask] = useState("");
    const [todos, setTodos] = useState([]);

    useEffect(() => {
        // Retrieve todos from local storage when the component mounts
        const storedTodos = JSON.parse(localStorage.getItem('todos'));
        if (storedTodos) {
          setTodos(storedTodos);
        }
      }, []);
    
      useEffect(() => {
        // Save todos to local storage whenever the todos state changes
        localStorage.setItem('todos', JSON.stringify(todos));
      }, [todos]);
    
      const handleInputChange = (event) => {
        setTask(event.target.value);
      };
    
      const handleAddTask = () => {
        if (task.trim() !== '') {
          setTodos([...todos, task]);
          setTask('');
        }
      };
    
      const handleRemoveTask = (index) => {
        const updatedTodos = [...todos];
        updatedTodos.splice(index, 1);
        setTodos(updatedTodos);
      };
    
      return (
        <div>
          <h2>You've got werk!</h2>
          <div>
            <input type="text" value={task} onChange={handleInputChange} />
            <button onClick={handleAddTask}>Add Task</button>
          </div>
          <ul>
            {todos.map((todo, index) => (
              <li key={index}>
                {todo}
                <button onClick={() => handleRemoveTask(index)}>Remove</button>
              </li>
            ))}
          </ul>
        </div>
      );
    };
    
    export default TodoList;
import "./App.css";
import { BrowserRouter as Router, Route, Link, Routes } from "react-router-dom";
import ParentComponent from "./components/ParentComponent";
import ChildComponent from "./components/ChildComponent";
import Count from "./components/CountComponent";
import WeatherComponent from "./components/FromApi";
import NavBar from "./components/NavBar";
import NameForm from "./components/NameForm";
import TodoList from "./components/TodoList";

function App() {
  return (
    <>
      <Router>
        <div>
          <NavBar />
          <div>
            <Routes>
              <Route path="/weather" element={<WeatherComponent />} />
              <Route path="/todo" element={<TodoList/>}/>
              <Route path="/nameform" element={<NameForm/>}/>
              <Route path="/" element={[<ParentComponent />,<ChildComponent />,<Count />]}/>
            </Routes>
          </div>
        </div>
      </Router>
    </>
  );
}

export default App;

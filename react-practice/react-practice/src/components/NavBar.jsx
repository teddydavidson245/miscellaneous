import { Link } from "react-router-dom";

const NavBar = () => {
  return (
    <nav className="navbar">
      <ul>
      <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/weather">Weather</Link>
        </li>
        <li>
          <Link to="/todo">Chores</Link>
        </li>
        <li>
          <Link to="/nameform">User</Link>
        </li>
      </ul>
    </nav>
  );
};

export default NavBar;

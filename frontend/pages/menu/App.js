import { BrowserRouter, Route } from "react-router-dom";
import Dashboard from "../dashboard/index";
import Login from "../login/index";
import Navbar from "../navbar/index";
import Register from "../register/index";

function App() {
  return (
    <BrowserRouter>
        <Route exact path="/login">
          <Login/>
        </Route>
        <Route path="/register">
          <Register/>
        </Route>
        <Route path="/dashboard">
          <Navbar/>
          <Dashboard/>
        </Route>
    </BrowserRouter>
  );
}

export default App;

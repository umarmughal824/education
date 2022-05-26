import React from 'react';
import logo from './logo.svg';
import axios from 'axios';
import { Routes, Route, BrowserRouter as Router, Link } from 'react-router-dom';
import './App.css';
import { routes } from "./urls"
import Welcome from "./components/Welcome"
import Home from "./components/Home"
import CreateQuiz from "./components/CreateQuiz"
import Quizes from "./components/Quizes"
import QuizDetails from "./components/QuizDetails"


function App() {
  return (
    <div className="App">
      <Router>
      <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/hello">Hello</Link>
          </li>
          <li>
            <Link to="/quizes">Quizes</Link>
          </li>
          <li>
            <Link to="/create-quiz">Create Quiz</Link>
          </li>
        </ul>

        <hr />
        <Routes>
          <Route
            path={routes.root}
            element={<Home />} 
          />
          <Route
            path={routes.hello}
            element={<Welcome />} 
          />
          <Route
            path={routes.quizes}
            element={<Quizes />} 
          />
          <Route
            exact
            path={routes.quizDetail}
            element={<QuizDetails />} 
          />
          <Route
            path={routes.createQuiz}
            element={<CreateQuiz />} 
          />

        </Routes>
      </Router>
      </div>
  );
}

export default App;

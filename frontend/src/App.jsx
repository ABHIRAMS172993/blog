import { useState, useEffect } from "react";

import "./App.css";
import Header from "./Header";
import Content from "./Content";

function App() {
  

  return (
    <>
    <Header />
    <Content />
    <button className="btn bg-blue-800 text-shadow-white p-4 border -2 text-white m-4 cursor-pointer">Create a blog</button>
      </>
  );
}

export default App;
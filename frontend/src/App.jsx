import { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [storeData, setStoreData] = useState([]);

  useEffect(() => {
    axios
      .get(import.meta.env.VITE_API_URL)
      .then((res) => {
        setStoreData(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  }, []);

  return (
    <>
      {storeData.map((item) => (
        <div key={item.id}>
          <h2>{item.title}</h2>
          <p>{item.subtitle}</p>
          <p>{item.content}</p>
          <p>{`Item created at: ${item.created_at.substring(0,10)}`}</p>
          <p>{`Item updated at: ${item.updated_at.substring(0,10)}`}</p>
        </div>
      ))}
    </>
  );
}

export default App;
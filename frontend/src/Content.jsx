import React,{useState,useEffect} from 'react'
import axios from "axios";

const Content = () => {


    const [storeData, setStoreData] = useState([]);

  useEffect(() => {
    console.log(import.meta.env.VITE_API_URL);
    axios
      // .get(import.meta.env.VITE_API_URL)
      .get('http://127.0.0.1:8000/')
      .then((res) => {
        setStoreData(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  }, []);

  return (
    <div className = "container text-shadow-2xs grid grid-cols-4 m-4 p-4 gap-4">
      {storeData.map((item) => (
        <div key={item.id} className="border-2 p-4 bg-violet-500">
          <h2 className="">{item.title}</h2>
          <p>{item.subtitle}</p>
          <p>{item.content}</p>
          <p>{`Item created at: ${item.created_at.substring(0,10)}`}</p>
          <p>{`Item updated at: ${item.updated_at.substring(0,10)}`}</p>
        </div>
      ))}
    </div>

  )
}


export default Content
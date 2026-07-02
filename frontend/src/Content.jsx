import React,{useState,useEffect} from 'react'
import axios from "axios";

const Content = () => {


    const [storeData, setStoreData] = useState([]);

  useEffect(() => {
    console.log(import.meta.env.VITE_API_URL);
    axios
      .get(import.meta.env.VITE_API_URL)
      // .get('http://127.0.0.1:8000/')
      .then((res) => {
        setStoreData(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  }, []);

  return (
    <div className = "container text-shadow-2xs grid grid-cols-4 m-4 p-4 gap-4 ">
      {storeData.map((item) => (
        <div key={item.id} className="border-1 w-[98vw] max-w-screen-xl p-4">
          <h2 className="font-[Poppins] text-4xl font-bold">{item.title}</h2>
          <p className='font-[Inter] text-lg text-gray-600 mt-2'>{item.subtitle}</p>
          <p className='font-[Merriweather] text-base leading-8 mt-6'>{item.content.substring(0,250)+"..."}<a href='#' className='text-yellow-500'> View more </a></p>
        
        </div>
      ))}
    </div>

  )
}


export default Content
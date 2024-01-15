import React from "react";
import { useState, useEffect} from "react";
import axios from 'axios'

const WeatherComponent = () => {
    const [weatherData, setWeatherData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error,setError] = useState(null);

    useEffect( ()=>{
        const featchWeatherData = async ()=> {
            try {
                const apiKey = "a57320f457424264b5f202900232012"
                const response = await axios.get(`https://api.weatherapi.com/v1/current.json?key=${apiKey}&q=Austin`)
                // const response = await axios.get('https://fakestoreapi.com/products/1')
                setWeatherData(response.data);
            } catch (error) {
                setError(error);
            } finally{
                setLoading(false);
            }
        };
        featchWeatherData();
    }, [] );

        if (loading) {
            return <p>Loading...</p>;
        }

        if (error) {
            return <p>Error: {error.message}</p>;
        }

  return(
    <div>
        {weatherData && (
            <div>
                <h2>Weather Information</h2>
                <p>Location: {weatherData.location.name}, {weatherData.location.region}, {weatherData.location.country}</p>
                <p>Temperature: {weatherData.current.temp_c}°C/{weatherData.current.temp_f}°F</p>
                <p>Feels like: {weatherData.current.feelslike_c}°C/{weatherData.current.feelslike_f}°F</p>
                <p>Condition: {weatherData.current.condition.text}</p>
                <p> <img src={weatherData.current.condition.icon} alt="weather icon" /></p>
            </div>
        )}
    </div>
  );
        }
  export default WeatherComponent;
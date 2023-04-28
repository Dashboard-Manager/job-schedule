import './Home.css';
import { useState } from 'react';

const Home = () => {
    const [count, setCount] = useState(0);
    const handleCount = () => {
        setCount((prevCount) => prevCount + 1);
    };

    return (
        <div className='Home'>
            <p>HomePage</p>
            <p>Number of clicks: {count}</p>
            <button onClick={handleCount}>Click me!</button>
            <ul className='list-disc'>
                <li className='mb-2'>
                    <a href='/register'>Register</a>
                </li>
                <li className='mb-2'>
                    <a href='/login'>Login</a>
                </li>
                <li className='extra mb-2'>
                    <a href='/extra'>Extra</a>
                </li>
            </ul>
        </div>
    );
};

export default Home;

import { useState } from 'react';

import './Login.css';

interface LoginProps {
    onLoginSuccess: (username: string, password: string) => void;
}

function Login({ onLoginSuccess }: LoginProps) {
    const [username, setUserName] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        if (username && password) {
            if (username === 'admin' && password === 'password') {
                onLoginSuccess(username, password);
            } else {
                setError('Invalid username or password');
            }
        }
    };

    return (
        <div className="container">
            <div className="login-wrapper">
                <h1>Please Log In</h1>
                {error && <p className="error">{error}</p>}
                <form onSubmit={handleSubmit}>
                    <label>
                        <p>Username</p>
                        <input
                            name="username"
                            type="text"
                            value={username}
                            onChange={(e) => setUserName(e.target.value)}
                        />
                    </label>
                    <label>
                        <p>Password</p>
                        <input
                            name="password"
                            type="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                        />
                    </label>
                    <div>
                        <button name="submit" type="submit">
                            Log In
                        </button>
                    </div>
                </form>
            </div>
        </div>
    );
}

export default Login;

import React, { useState } from 'react'
import axios from "axios";

const Register = () => {
    const [username, setUsername] = useState('string');
    const [email, setEmail] = useState('user@example.com');
    const [password1, setPassword] = useState('ExtraPassword12345!');
    const [password2, setConfPassword] = useState('ExtraPassword12345!');
    const [msg, setMsg] = useState('');

    const registerURL = 'http://127.0.0.1:8000/api/auth/register/'

    const Register = async (e) => {
        e.preventDefault();
        try {
            await axios.post(registerURL, {
                username: username,
                email: email,
                password1: password1,
                password2: password2
            })
                .then(response => {
                    return (
                        console.log(response)
                    )
                });
        } catch (error) {
            if (error.response) {
                setMsg(error.response.data.msg);
            }
        }
    }

    return (
        <section className="hero has-background-grey-light is-fullheight is-fullwidth">
            <div className="hero-body">
                <div className="container">
                    <div className="columns is-centered">
                        <div className="column is-4-desktop">
                            <form onSubmit={Register} className="box">
                                <p className="has-text-centered">{msg}</p>
                                <div className="field mt-5">
                                    <div className="controls">
                                        <input type="text" className="input" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} />
                                    </div>
                                </div>
                                <div className="field mt-5">
                                    <div className="controls">
                                        <input type="text" className="input" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
                                    </div>
                                </div>
                                <div className="field mt-5">
                                    <div className="controls">
                                        <input type="password" className="input" placeholder="******" value={password1} onChange={(e) => setPassword(e.target.value)} />
                                    </div>
                                </div>
                                <div className="field mt-5">
                                    <div className="controls">
                                        <input type="password" className="input" placeholder="******" value={password2} onChange={(e) => setConfPassword(e.target.value)} />
                                    </div>
                                </div>
                                <div className="field mt-5">
                                    <button className="button is-success is-fullwidth">Register</button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    )
}

export default Register

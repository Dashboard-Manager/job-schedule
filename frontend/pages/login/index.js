import React, { useState } from "react";
("react-dom");
import axios from "axios";

const Login = () => {
    const [username, setUsername] = useState("admin");
    const [email, setEmail] = useState("admin@admin.com");
    const [password, setPassword] = useState("admin");
    const [msg, setMsg] = useState("");

    const loginURL = "http://localhost:8000/api/auth/login/";

    const Auth = async (e) => {
        e.preventDefault();
        try {
            await axios
                .post(loginURL, {
                    username: username,
                    email: email,
                    password: password,
                })
                .then((response) => {
                    axios.defaults.headers.common[
                        "Authorization"
                    ] = `Bearer ${response.data.access_token}`;
                    axios.defaults.headers.common[
                        "Set-Cookie"
                    ] = `token=${response.data.access_token}; HttpOnly; Secure`;
                    axios.defaults.headers.post[
                        "Authorization"
                    ] = `Bearer ${response.data.access_token}`;
                    return console.log(response);
                });
        } catch (error) {
            if (error.response) {
                setMsg(error.response.data.msg);
            }
        }
    };

    return (
        <section className="hero has-background-grey-light is-fullheight is-fullwidth">
            <div className="hero-body">
                <div className="container">
                    <div className="columns is-centered">
                        <div className="column is-4-desktop">
                            <form onSubmit={Auth} className="box">
                                <p className="has-text-centered">{msg}</p>
                                <div className="field mt-5">
                                    <div className="controls">
                                        <input
                                            type="text"
                                            className="input"
                                            placeholder="Username"
                                            value={username}
                                            onChange={(e) =>
                                                setUsername(e.target.value)
                                            }
                                        />
                                    </div>
                                </div>
                                <div className="field mt-5">
                                    <div className="controls">
                                        <input
                                            type="text"
                                            className="input"
                                            placeholder="Email"
                                            value={email}
                                            onChange={(e) =>
                                                setEmail(e.target.value)
                                            }
                                        />
                                    </div>
                                </div>
                                <div className="field mt-5">
                                    <div className="controls">
                                        <input
                                            type="password"
                                            className="input"
                                            placeholder="******"
                                            value={password}
                                            onChange={(e) =>
                                                setPassword(e.target.value)
                                            }
                                        />
                                    </div>
                                </div>
                                <div className="field mt-5">
                                    <button className="button is-success is-fullwidth">
                                        Login
                                    </button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    );
};

export default Login;

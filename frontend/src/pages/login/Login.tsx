import { useState } from 'react'
import './Login.css'

interface LoginProps {
  onLoginSuccess: (userName: string, password: string) => void
}

export function Login({ onLoginSuccess }: LoginProps) {
  const [userName, setUserName] = useState('admin')
  const [password, setPassword] = useState('')

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault()
    if (userName && password) {
      onLoginSuccess(userName, password)
    }
  }

  return (
    <div className='container'>
      {/* <div className='login-wrapper'>
        <h1>Please Log In</h1>
        <form onSubmit={handleSubmit}>
          <label>
            <p>Username</p>
            <input type='text' value={userName} onChange={(e) => setUserName(e.target.value)} />
          </label>
          <label>
            <p>Password</p>
            <input type='password' value={password} onChange={(e) => setPassword(e.target.value)} />
          </label>
          <div>
            <button type='submit'>Log In</button>
          </div>
        </form>
      </div> */}
    </div>
  )
}

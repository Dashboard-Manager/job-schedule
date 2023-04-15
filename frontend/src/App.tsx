import { Dashboard } from 'pages/Dashboard'
import { Login } from 'pages/Login'
import { Register } from 'pages/Register'
import { BrowserRouter, Route, Routes } from 'react-router-dom'

export function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Dashboard />} />
        <Route path='/login' element={<Login />} />
        <Route path='/register' element={<Register />} />
      </Routes>
    </BrowserRouter>
  )
}

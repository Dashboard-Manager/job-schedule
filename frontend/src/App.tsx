import { Dashboard } from 'pages/Dashboard'
import { Login } from 'pages/Login'
import { Register } from 'pages/register/Register'
import { BrowserRouter, Route, Routes } from 'react-router-dom'

export function App() {
  // const handleLoginSuccess = (userName: string, password: string) => {
  //   console.log(userName, password);
  // };

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/login" element={< Login />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </BrowserRouter>
  );
}

// interface LoginWrapperProps {
//   onLoginSuccess: (userName: string, password: string) => void;
// }

// function LoginWrapper({ onLoginSuccess }: LoginWrapperProps) {
//   return <Login onLoginSuccess={onLoginSuccess} />;
// }

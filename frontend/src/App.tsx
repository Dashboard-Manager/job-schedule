import { Dashboard } from 'pages/Dashboard'
import { Login } from 'pages/Login'
// =======
// import { Login } from 'pages/login/Login'
// >>>>>>> a73d3f729150e96aa87811b2510e1c565681fee3
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
{/* =======
        <Route path="/login" element={<LoginWrapper onLoginSuccess={handleLoginSuccess} />} />
>>>>>>> a73d3f729150e96aa87811b2510e1c565681fee3 */}
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

// interface LoginWrapperProps {
//   onLoginSuccess: (userName: string, password: string) => void;
// }

// function LoginWrapper({ onLoginSuccess }: LoginWrapperProps) {
//   return <Login onLoginSuccess={onLoginSuccess} />;
// }

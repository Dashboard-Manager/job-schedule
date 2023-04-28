import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { ReactQueryDevtools } from '@tanstack/react-query-devtools';
import Home from 'pages/home/Home';
import { Login } from 'pages/users/login/Login';
import Register from 'pages/users/register/Register';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import PrivateRoutes from 'utils/PrivateRoutes';

const queryClient = new QueryClient();

function App() {
    return (
        <QueryClientProvider client={queryClient}>
            <BrowserRouter>
                <Routes>
                    <Route element={<PrivateRoutes />}>
                        <Route path='/extra' />
                    </Route>
                    <Route path='/register' element={<Register />} />
                    <Route path='/' element={<Home />} />
                    <Route path='/login' element={<Login />} />
                </Routes>
                <ReactQueryDevtools initialIsOpen={false} />
            </BrowserRouter>
        </QueryClientProvider>
    );
}

export default App;

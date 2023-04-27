import { Login } from 'pages/users/login/Login';
import { render, screen } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';

describe('Login component', () => {
    test('should render all input fields and login button', () => {
        render(
            <BrowserRouter>
                <Login />
            </BrowserRouter>
        );

        const nameInput = screen.getByLabelText(/name/i);
        const usernameInput = screen.getByLabelText(/username/i);
        const passwordInput = screen.getByLabelText(/password/i);
        const loginButton = screen.getByRole('button', { name: /login/i });

        expect(nameInput).toBeInTheDocument();
        expect(usernameInput).toBeInTheDocument();
        expect(passwordInput).toBeInTheDocument();
        expect(loginButton).toBeInTheDocument();
    });
});

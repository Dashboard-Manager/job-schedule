/**
 * @jest-environment jsdom
 */
import { fireEvent, render, screen } from '@testing-library/react'
import { BrowserRouter } from 'react-router-dom'
import Login from '../../pages/users/login/Login'

describe('Login component', () => {
    test('should render all input fields and login button', () => {
        render(
            <BrowserRouter>
                <Login />
            </BrowserRouter>,
        )

        const nameInput = screen.getByLabelText(/name/i)
        const usernameInput = screen.getByLabelText(/username/i)
        const passwordInput = screen.getByLabelText(/password/i)
        const loginButton = screen.getByRole('button', { name: /login/i })

        expect(nameInput).toBeInTheDocument()
        expect(usernameInput).toBeInTheDocument()
        expect(passwordInput).toBeInTheDocument()
        expect(loginButton).toBeInTheDocument()
    })

    test('should submit the form with correct values', () => {
        render(
            <BrowserRouter>
                <Login />
            </BrowserRouter>,
        )

        const usernameInput = screen.getByLabelText(/username/i)
        const passwordInput = screen.getByLabelText(/password/i)
        const loginButton = screen.getByRole('button', { name: /login/i })

        fireEvent.change(usernameInput, { target: { value: 'john@example.com' } })
        fireEvent.change(passwordInput, { target: { value: 'password123' } })

        fireEvent.click(loginButton)

        expect(usernameInput).toHaveValue('john@example.com')
        expect(passwordInput).toHaveValue('password123')
    })
})

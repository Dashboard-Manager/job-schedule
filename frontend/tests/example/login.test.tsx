/**
 * @jest-environment jsdom
 */

import { fireEvent, render } from '@testing-library/react'
import Login from '../../src/pages/login/Login'

test('submitting valid credentials calls onLoginSuccess', () => {
    const onLoginSuccessMock = jest.fn()
    const { getByLabelText, getByText } = render(<Login onLoginSuccess={onLoginSuccessMock} />)

    const usernameInput = getByLabelText('Username')
    fireEvent.change(usernameInput, { target: { value: 'admin' } })

    const passwordInput = getByLabelText('Password')
    fireEvent.change(passwordInput, { target: { value: 'password' } })

    const loginButton = getByText('Log In')
    fireEvent.click(loginButton)

    expect(onLoginSuccessMock).toHaveBeenCalledWith('admin', 'password')
})

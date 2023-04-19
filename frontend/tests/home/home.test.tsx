/**
 * @jest-environment jsdom
 */

import '@testing-library/jest-dom'
import { cleanup, fireEvent, render, screen } from '@testing-library/react'
import Home from '../../src/pages/Home'

afterEach(() => {
    cleanup()
})

describe('App Component', () => {
    // Test 1
    test('App Rendering', () => {
        render(<Home />) // Rendering the Home
        const text = screen.getByTestId('text')
        const button = screen.getByTestId('button')
        expect(button).toBeInTheDocument()
        expect(text).toBeInTheDocument()
    })

    // Test 2
    test('Default Text', () => {
        render(<Home />)
        const text = screen.getByTestId('text')
        expect(text).toHaveTextContent('GeeksForGeeks')
    })

    // Test 3
    test('Toggling Text', () => {
        render(<Home />)
        const text = screen.getByTestId('text')
        const button = screen.getByTestId('button')
        expect(text).toHaveTextContent('GeeksForGeeks')
        fireEvent.click(button)
        expect(text).toBeEmptyDOMElement()
        fireEvent.click(button)
        expect(text).toHaveTextContent('GeeksForGeeks')
    })
})

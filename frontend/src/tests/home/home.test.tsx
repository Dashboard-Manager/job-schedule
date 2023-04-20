/**
 * @jest-environment jsdom
 */

import { render, screen } from '@testing-library/react'
import Home from '../../pages/home/Home'

describe('Home', () => {
    it('should render the HomePage text', () => {
        render(<Home />)
        expect(screen.getByText('HomePage')).toBeInTheDocument()
    })

    it('should render the Register and Login links', () => {
        render(<Home />)
        expect(screen.getByRole('link', { name: 'Register' })).toHaveAttribute('href', '/register')
        expect(screen.getByRole('link', { name: 'Login' })).toHaveAttribute('href', '/login')
    })

    it('should apply margin-bottom to each list item', () => {
        render(<Home />)
        const listItems = screen.getAllByRole('listitem')
        listItems.forEach((item) => {
            expect(item).toHaveClass('mb-2')
        })
    })
})

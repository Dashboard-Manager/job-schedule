import '../support/commands'

describe('Login form', () => {
    beforeEach(() => {
        cy.visit('/login')
    })

    it('allows the user to log in with valid credentials', () => {
        cy.login('admin', 'password')
        cy.url().should('equal', 'http://localhost:3000/login')
    })

    it('displays an error message if the user enters invalid credentials', () => {
        cy.login('invalid', 'invalid')
        cy.contains('Invalid username or password').should('be.visible')
    })
})

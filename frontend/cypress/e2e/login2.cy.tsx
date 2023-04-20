Cypress.Commands.add('login', (username, password) => {
    cy.visit('/login2')
    cy.get('[name="username"]').type(username)
    cy.get('[name="password"]').type(password)
    cy.get('form').submit()
})

describe('Login form', () => {
    beforeEach(() => {
        cy.visit('/login2')
    })

    it('allows the user to log in with valid credentials', () => {
        cy.login('admin', 'password')
        cy.url().should('equal', 'http://localhost:3000/login2')
    })

    it('displays an error message if the user enters invalid credentials', () => {
        cy.login('invalid', 'invalid')
        cy.contains('Invalid username or password').should('be.visible')
    })
})

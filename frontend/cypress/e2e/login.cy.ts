import user_data from '../fixtures/user_data.json';
import '../support/commands';

describe('Login form', () => {
    beforeEach(() => {
        cy.visit('/login');
    });

    it('allows the user to log in with valid credentials', () => {
        cy.login(user_data.username, user_data.password);
        cy.url().should('equal', 'http://localhost:3000/login');
    });

    it('displays an alert message with the entered username and password if the user enters invalid credentials', () => {
        // spy on the alert function and intercept the network request
        cy.window().then((win) => {
            cy.spy(win, 'alert').as('onAlert');
        });
        cy.intercept('POST', '/login', {
            statusCode: 401,
            body: {message: 'Invalid username or password'},
        }).as('loginRequest');

        cy.get('[name="username"]').type(user_data.username);
        cy.get('[name="password"]').type(user_data.password);
        cy.get('form').submit();

        // wait for the alert to be displayed and check the message
        cy.get('@onAlert').should('have.been.calledOnce');
    });
});

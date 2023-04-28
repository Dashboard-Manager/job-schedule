Cypress.Commands.add('login', (username, password) => {
    cy.visit('/login');
    cy.get('[name="username"]').type(username);
    cy.get('[name="password"]').type(password);
    cy.get('form').submit();
});

import { defineConfig } from 'cypress';

export default defineConfig({
    video: false,
    e2e: {
        baseUrl: 'http://localhost:3000',
        supportFile: './cypress/support/commands.ts',
    },
});

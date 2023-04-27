import react from '@vitejs/plugin-react';
import path from 'path';
import eslint from 'vite-plugin-eslint';
import tsconfigPaths from 'vite-tsconfig-paths';
import { defineConfig } from 'vitest/config';

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [react(), tsconfigPaths(), eslint()],
    test: {
        globals: true,
        environment: 'jsdom',
        setupFiles: './src/vitest-setup.tsx',
        coverage: {
            reportsDirectory: '../coverage/',
            provider: 'c8',
        },
    },
    resolve: {
        alias: {
            '@': path.resolve(__dirname, './src/'),
            components: path.resolve(__dirname, './src/components/'),
            schemas: path.resolve(__dirname, './src/schemas/'),
            utils: path.resolve(__dirname, './src/utils/'),
            public: path.resolve(__dirname, './public'),
            pages: path.resolve(__dirname, './src/pages'),
            types: path.resolve(__dirname, './src/@types'),
        },
    },
    server: {
        watch: {
            usePolling: true,
        },
        host: '0.0.0.0',
        port: 3000,
    },
});

// @ts-check
import { defineConfig } from 'eslint-define-config';

module.exports = defineConfig({
    root: true,
    env: {
        node: true,
        browser: true,
        es2021: true,
        'cypress/globals': true,
    },
    extends: [
        'react-app',
        'eslint:recommended',
        'plugin:import/recommended',
        'plugin:import/typescript',
        'plugin:jest-dom/recommended',
        'plugin:react/recommended',
        'plugin:react-hooks/recommended',
        'plugin:tailwindcss/recommended',
        'plugin:@typescript-eslint/recommended',
        'plugin:@tanstack/eslint-plugin-query/recommended',
        'plugin:cypress/recommended',
        'plugin:promise/recommended',
    ],
    plugins: [
        'react',
        'react-hooks',
        'react-refresh',
        'tailwindcss',
        'cypress',
        'prettier',
        'promise',
    ],
    overrides: [
        {
            files: ['*.ts', '*.tsx', '*.js'],
            parser: '@typescript-eslint/parser',
        },
    ],
    parserOptions: {
        ecmaVersion: 2021,
        sourceType: 'module',
        ecmaFeatures: {
            jsx: true,
        },
    },
    rules: {
        'react-refresh/only-export-components': ['warn', { checkJS: true }],
        'react/react-in-jsx-scope': 'off',
        '@typescript-eslint/no-redeclare': 'off',
        'tailwindcss/no-custom-classname': 'off',
        'cypress/no-assigning-return-values': 'error',
        'cypress/no-unnecessary-waiting': 'error',
        'cypress/assertion-before-screenshot': 'warn',
        'cypress/no-force': 'warn',
        'cypress/no-async-tests': 'error',
        'cypress/no-pause': 'error',
        'prettier/prettier': 'error',
        'promise/always-return': 'error',
        'promise/no-return-wrap': 'error',
        'promise/param-names': 'error',
        'promise/catch-or-return': 'error',
        'promise/no-native': 'off',
        'promise/no-nesting': 'warn',
        'promise/no-promise-in-callback': 'warn',
        'promise/no-callback-in-promise': 'warn',
        'promise/avoid-new': 'warn',
        'promise/no-new-statics': 'error',
        'promise/no-return-in-finally': 'warn',
        'promise/valid-params': 'warn',
    },
    settings: {
        react: {
            version: 'detect',
        },
        'import/resolver': {
            typescript: true,
            node: true,
        },
    },
});

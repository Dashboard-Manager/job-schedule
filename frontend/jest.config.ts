/* eslint-disable */
import type { Config } from '@jest/types';
import { defaults as tsJestPreset } from 'ts-jest/presets';

const config: Config.InitialOptions = {
    roots: ['<rootDir>/src'],
    testEnvironmentOptions: {
        url: 'http://localhost/3000',
    },
    preset: 'ts-jest',
    testEnvironment: 'node',
    verbose: true,
    bail: 1,
    ...tsJestPreset,
    testMatch: [
        '<rootDir>/**/(*.)test.(js|jsx|ts|tsx)',
        '<rootDir>/src/**/__tests__/**/*.{js,jsx,ts,tsx}',
        '<rootDir>/src/**/*.{spec,test}.{js,jsx,ts,tsx}',
    ],
    transform: {
        ...tsJestPreset.transform,
        '^.+\\.(css|styl|less|sass|scss)$': 'jest-css-modules-transform',
        '^.+\\.tsx?$': 'ts-jest',
    },
    moduleFileExtensions: ['ts', 'tsx', 'js', 'jsx', 'json', 'node'],
    moduleDirectories: ['node_modules', 'src'],
    setupFilesAfterEnv: [
        '@testing-library/jest-dom/extend-expect',
        '@testing-library/jest-dom',
    ],
    clearMocks: true,
    restoreMocks: true,
    collectCoverage: true,
    coverageDirectory: '../coverage/',
    coverageProvider: 'v8',
    coverageThreshold: {
        global: {
            branches: 80,
            functions: 80,
            lines: 80,
            statements: 80,
        },
    },
};

export default config;

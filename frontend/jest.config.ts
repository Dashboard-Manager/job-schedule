/* eslint-disable */
import type { Config } from '@jest/types'
import { defaults as tsjPreset } from 'ts-jest/presets'

const config: Config.InitialOptions = {
    preset: 'ts-jest',
    testEnvironment: 'node',
    verbose: true,
    bail: 1,
    ...tsjPreset,
    testMatch: [
        '**/__tests__/**/*.[jt]s?(x)',
        '**/?(*.)+(spec|test).[jt]s?(x)',
        '<rootDir>/tests/**/*.[jt]s?(x)',
    ],
    transform: {
        ...tsjPreset.transform,
        '^.+\\.[tj]sx?$': 'ts-jest',
        '^.+\\.(css|styl|less|sass|scss)$': 'jest-css-modules-transform',
    },
    rootDir: './tests/',
    moduleFileExtensions: ['ts', 'tsx', 'js', 'jsx', 'json', 'node'],
    moduleDirectories: ['node_modules', '<rootDir>/'],
    setupFilesAfterEnv: ['@testing-library/jest-dom/extend-expect', '@testing-library/jest-dom'],
    clearMocks: true,
    restoreMocks: true,
    collectCoverage: true,
    coverageDirectory: '../coverage/',
    coverageProvider: 'v8',
}

export default config

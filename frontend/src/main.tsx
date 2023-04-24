import { StrictMode } from 'react';
import App from './App';
import './App.css';
import './input.css';
import { createRoot } from 'react-dom/client';

const root = createRoot(document.getElementById('root') as HTMLElement);
root.render(
    <StrictMode>
        <App />
    </StrictMode>
);

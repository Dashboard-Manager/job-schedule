import { ReactNode } from 'react';

export function DescriptionTypography({ children }: { children: ReactNode }) {
    return (
        <p className="mb-8 text-center text-sm text-secondary-text">
            {children}
        </p>
    );
}

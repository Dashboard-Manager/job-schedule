import { ReactNode } from 'react';

export function DescriptionTypography({ children }: { children: ReactNode }) {
    return (
        <p className='text-secondary-text mb-8 text-center text-sm'>
            {children}
        </p>
    );
}

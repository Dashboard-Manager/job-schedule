import { ReactNode } from 'react';

export function Board({ children }: { children: ReactNode }) {
    return (
        <div className='sm:h-400 w-full max-w-[400px] rounded-xl bg-gray-dark p-8 first-letter:text-white-text'>
            {children}
        </div>
    );
}

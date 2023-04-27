import { ReactNode } from 'react';

export function Board({ children }: { children: ReactNode }) {
    return (
        <div className='sm:h-400 bg-gray-dark first-letter:text-white-text w-full max-w-[400px] rounded-xl p-8'>
            {children}
        </div>
    );
}

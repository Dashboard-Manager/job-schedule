import { ReactNode } from 'react';

export function Board({ children }: { children: ReactNode }) {
    return (
        <div className='h-full·w-full·max-w-[400px]·rounded-xl·bg-gray-dark··p-8·text-white-text'>
            {children}
        </div>
    );
}

import { ReactNode } from 'react'

export function Button({
  children,
  type = 'button',
}: {
  children: ReactNode
  type: 'button' | 'submit' | 'reset' | undefined
}) {
  return (
    <button type={type} className='bg-bloody px-8 py-2 font-bold active:translate-y-[1px] '>
      {children}
    </button>
  )
}

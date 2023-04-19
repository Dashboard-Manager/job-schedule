import { MouseEvent, ReactNode } from 'react'

type Button = {
  children: ReactNode
  type: 'button' | 'submit' | 'reset' | undefined
}

export function Button({ children, type = 'button' }: Button) {
  const handleClick = (event: MouseEvent<HTMLButtonElement>) => {
    const button = event.target as HTMLButtonElement
    button.blur()
  }

  return (
    <button
      type={type}
      className={
        'bg-bloody px-8 py-2 font-bold outline-none  focus:bg-blue-500 active:translate-y-[1px]'
      }
      onClick={handleClick}
    >
      {children}
    </button>
  )
}

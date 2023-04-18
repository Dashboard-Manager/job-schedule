import { fontFormStyles } from 'utils'
import { ReactNode, useRef, useState, FocusEvent } from 'react'
import { FormikHandlers } from 'formik'

export function FormElement({
  type,
  name,
  icon,
  value,
  onChange,
  onBlur,
}: {
  type: string
  name: string
  icon: ReactNode
  value: string
  onChange: FormikHandlers['handleChange']
  onBlur: FormikHandlers['handleBlur']
}) {
  const input = useRef<HTMLInputElement>(null)
  const [isFocused, setIsFocused] = useState(false)

  const focusInput = () => {
    if (input.current !== null) {
      input.current.focus()
    }
  }

  return (
    <div className='mb-4'>
      <label htmlFor={name}>{name}</label>
      <div
        className={`flex items-center border-2 bg-gray-light p-2
        ${isFocused ? 'border-bloody' : ' border-gray-dark'}`}
      >
        <input
          type={type}
          id={name}
          name={name}
          onChange={onChange}
          value={value}
          placeholder={name}
          className='order-2 bg-gray-light outline-none'
          style={{
            fontSize: `${fontFormStyles.size}`,
          }}
          ref={input}
          onBlur={(e) => setIsFocused(false)}
          onFocus={() => setIsFocused(true)}
        />
        <span className='order-1 cursor-text px-2' aria-hidden onClick={focusInput}>
          {icon}
        </span>
      </div>
    </div>
  )
}

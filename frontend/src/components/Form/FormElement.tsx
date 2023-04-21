import {Tooltip} from '../Tooltip';
import {FormikHandlers} from 'formik';
import {ReactNode, useRef, useState} from 'react';
import {fontFormStyles} from 'utils';

type FormElement = {
    type: string;
    name: string;
    icon: ReactNode;
    value: string;
    onChange: FormikHandlers['handleChange'];
    error?: string | undefined;
    touched?: boolean | undefined;
};

export function FormElement({
    type,
    name,
    icon,
    value,
    onChange,
    error,
    touched,
}: FormElement) {
    const input = useRef<HTMLInputElement>(null);
    const [isFocused, setIsFocused] = useState(false);

    const focusInput = () => {
        if (input.current !== null) {
            input.current.focus();
        }
    };

    return (
        <>
            <div className="relative mb-4">
                <label htmlFor={name}>{name}</label>
                <div
                    className={`flex items-center border-2 bg-gray-light p-2
        ${
            isFocused
                ? 'border-blue-500'
                : error
                ? 'border-bloody'
                : 'border-gray-dark'
        }`}>
                    <input
                        type={type}
                        id={name}
                        name={name}
                        onChange={onChange}
                        value={value}
                        placeholder={name}
                        className="order-2 bg-gray-light outline-none"
                        style={{
                            fontSize: `${fontFormStyles.size}`,
                        }}
                        ref={input}
                        onBlur={() => setIsFocused(false)}
                        onFocus={() => setIsFocused(true)}
                    />
                    <span
                        className="order-1 cursor-text px-2"
                        aria-hidden
                        onClick={focusInput}>
                        {icon}
                    </span>
                </div>
                {touched && error && <Tooltip content={error} />}
            </div>
        </>
    );
}

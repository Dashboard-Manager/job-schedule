import React from 'react';

type ButtonProps = {
    setToggle: React.Dispatch<React.SetStateAction<boolean>>;
    btnTxt: string;
};

const Button = ({ setToggle, btnTxt }: ButtonProps) => {
    return (
        <button data-testid="button" onClick={() => setToggle((prev) => !prev)}>
            {btnTxt}
        </button>
    );
};

export default Button;

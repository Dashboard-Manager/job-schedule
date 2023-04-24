import { FaLock, FaUserAlt } from 'react-icons/fa';
import { MdAlternateEmail } from 'react-icons/md';

export const fontFormStyles = {
    size: '1.1em',
};

export const FormElements = {
    RegisterPage: [
        {
            id: 1,
            type: 'text',
            name: 'name',
            icon: <FaUserAlt color='#498afb' size={`${fontFormStyles.size}`} />,
        },
        {
            id: 2,
            type: 'text',
            name: 'username',
            icon: (
                <MdAlternateEmail
                    color='#9166cc'
                    size={`${fontFormStyles.size}`}
                />
            ),
        },
        {
            id: 3,
            type: 'password',
            name: 'password',
            icon: <FaLock color='#fa8142' size={`${fontFormStyles.size}`} />,
        },
    ],
    LoginPage: [
        {
            id: 1,
            type: 'text',
            name: 'username',
            icon: (
                <MdAlternateEmail
                    color='#9166cc'
                    size={`${fontFormStyles.size}`}
                />
            ),
        },
        {
            id: 2,
            type: 'password',
            name: 'password',
            icon: <FaLock color='#fa8142' size={`${fontFormStyles.size}`} />,
        },
    ],
};

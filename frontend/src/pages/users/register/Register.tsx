import { Button } from 'components/Button';
import { DescriptionTypography } from 'components/DescriptionTypography';
import { Board } from 'components/Form/Board';
import { FormElement } from 'components/Form/FormElement';
import { useFormik } from 'formik';
import { Link } from 'react-router-dom';
import { formSchema } from 'schemas/index';
import { FormElements } from 'utils/index';

function Register() {
    const { errors, handleChange, handleSubmit, touched, values } = useFormik({
        initialValues: {
            name: '',
            username: '',
            password: ''
        },
        validationSchema: formSchema,
        onSubmit: () => console.log('submitted')
    });

    return (
        <div className='bg-black-bg text-white-text flex h-[100vh] w-[100vw] items-center justify-center'>
            <Board>
                <h1 className='mb-2 text-center text-4xl font-bold'>
                    Register
                </h1>
                <DescriptionTypography>
                    Fill the form and play!
                </DescriptionTypography>
                <form onSubmit={handleSubmit}>
                    {FormElements.RegisterPage.map((input) => {
                        const valueOfElement =
                            input.name as keyof typeof values;

                        return (
                            <FormElement
                                key={input.id}
                                type={input.type}
                                name={input.name}
                                icon={input.icon}
                                value={values[valueOfElement]}
                                onChange={handleChange}
                                error={errors[valueOfElement]}
                                touched={touched[valueOfElement]}
                            />
                        );
                    })}
                    <div className='mb-2 mt-8 text-center'>
                        <Button type='submit'>Register</Button>
                    </div>
                </form>
                <DescriptionTypography>
                    Already have an account?{' '}
                    <Link className='text-success' to='/login'>
                        Log in.
                    </Link>{' '}
                </DescriptionTypography>
            </Board>
        </div>
    );
}

export default Register;

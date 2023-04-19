import { Button } from 'components/Button'
import { DescriptionTypography } from 'components/DescriptionTypography'
import { Board } from 'components/Form/Board'
import { FormElement } from 'components/Form/FormElement'
import { FormElements } from 'utils'
import { useFormik } from 'formik'
import { Link } from 'react-router-dom'

export function Login() {
  const { errors, handleChange, handleSubmit, touched, values } = useFormik({
    initialValues: {
      name: '',
      username: '',
      password: '',
    },
    onSubmit: (values) => {
      alert(JSON.stringify(values, null, 2))
    },
  })

  return (
    <div className='flex h-[100vh] w-[100vw] items-center justify-center bg-black-bg'>
      <Board>
        <h1 className='mb-2 text-center text-4xl font-bold'>Login</h1>
        <DescriptionTypography>Fill the form and play!</DescriptionTypography>
        <form onSubmit={handleSubmit}>
          {FormElements.LoginPage.map((input) => {
            const valueOfElement = input.name as keyof typeof values

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
            )
          })}
          <div className='mb-2 mt-8 text-center'>
            <Button type='submit'>Login</Button>
          </div>
        </form>
        <DescriptionTypography>
          Don&apos;t have an account ?{' '}
          <Link className='text-success' to='/register'>
            Create an account.
          </Link>{' '}
        </DescriptionTypography>
      </Board>
    </div>
  )
}

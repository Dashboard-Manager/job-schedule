import { Board } from 'components/Board'
import { Button } from 'components/Button'
import { DescriptionTypography } from 'components/DescriptionTypography'
import { FormElement } from 'components/FormElement'
import { FormElements } from 'utils'
import { useFormik } from 'formik'
import { Link } from 'react-router-dom'

export function Login() {
  const { handleBlur, handleChange, handleSubmit, values } = useFormik({
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
          {FormElements.LoginPage.map((element) => {
            const valueOfElement = element.name as keyof typeof values

            return (
              <FormElement
                key={element.id}
                type={element.type}
                name={element.name}
                icon={element.icon}
                value={values[valueOfElement]}
                onChange={handleChange}
                onBlur={handleBlur}
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

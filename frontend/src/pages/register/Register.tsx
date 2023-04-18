import { Board } from 'components/Board'
import { Button } from 'components/Button'
import { DescriptionTypography } from 'components/DescriptionTypography'
import { FormElement } from 'components/FormElement'
import { formSchema } from 'schemas'
import { FormElements } from 'utils'
import { useFormik } from 'formik'
import { Link } from 'react-router-dom'


export function Register() {
  const { handleBlur, handleChange, handleSubmit, values} = useFormik({
    initialValues: {
      name: '',
      username: '',
      password: '',
    },
    validationSchema: formSchema,
    onSubmit: () => console.log('submitted')
  })


  return (
    <div className='flex h-[100vh] w-[100vw] items-center justify-center bg-black-bg'>
      <Board>
        <h1 className='mb-2 text-center text-4xl font-bold'>Register</h1>
        <DescriptionTypography>Fill the form and play!</DescriptionTypography>
        <form onSubmit={handleSubmit}>
          {FormElements.RegisterPage.map((element) => {
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
  )
}

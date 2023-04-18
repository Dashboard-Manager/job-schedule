import * as yup from 'yup'

// const passwordRules = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d!@#$%^&*()_+~`\-={}[\]:;"'<>,.?/|]{6,16}$/

const passwordSchema = yup
  .string()
  .required('Password is required')
  .min(6, 'Password must be at least 6 characters')
  .max(16, 'Password cannot be more than 16 characters')
  .matches(/[a-z]/, 'Password must contain at least one lowercase letter')
  .matches(/[A-Z]/, 'Password must contain at least one uppercase letter')
  .matches(/\d/, 'Password must contain at least one number');

export function validatePassword(password: string): string[] | undefined {
  try {
    passwordSchema.validateSync(password, { abortEarly: false });
    return undefined;
  } catch (e) {
    if (e instanceof yup.ValidationError) {
      return e.errors;
    }
    throw e;
  }
}

export const formSchema = yup.object().shape({
  name: yup.string().required('This field is required'),
  username: yup.string().min(5).required('This field is required'),
  password: passwordSchema,
  confirmPassword: yup
    .string()
    .required('Password confirmation is required')
    .oneOf([yup.ref('password')], 'Passwords must match'),
});



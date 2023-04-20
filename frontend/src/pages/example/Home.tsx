import { useState } from 'react'
import Button from '../Button'
import Text from '../Text'

const Home = () => {
    const [toggle, setToggle] = useState(true)

    return (
        <div className='Home'>
            <Text toggle={toggle} displayTxt='GeeksForGeeks' />
            <Button setToggle={setToggle} btnTxt='Toggle Text' />
        </div>
    )
}

export default Home

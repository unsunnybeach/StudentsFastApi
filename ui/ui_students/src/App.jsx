import { useState } from 'react'
import { fetchStudents, createStudent } from './services/students'
import './App.css'


function App() {
  // const [count, setCount] = useState(0)

  createStudent({firstName: "TEST", lastName: "TEST 2"}).then(() => {
  fetchStudents().then((students) => console.log(students))
  })


  return (
    <>
        {/* <button onClick={() => setCount((count) => count + 1)}>
        Kliknełxś już {count} razy
        </button> */}

    </>
  )
}

export default App

import { Helmet, HelmetProvider } from 'react-helmet-async'
// import { RouterProvider } from 'react-router-dom'
import { router } from './router'
import { RouterProvider } from 'react-router-dom'

function App() {
  return (
    <>
       <HelmetProvider>
        <Helmet />
          <title>Recomendador</title>
        <RouterProvider router={router} />
      </HelmetProvider>
    </>
  )
}

export default App

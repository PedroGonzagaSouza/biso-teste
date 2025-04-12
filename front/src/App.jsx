import { Helmet, HelmetProvider } from 'react-helmet-async'
import { router } from './router'
import { RouterProvider } from 'react-router-dom'

import { AuthProvider } from './AuthContext'
function App() {
  return (
    <>
      <HelmetProvider>
        <AuthProvider>
          <Helmet />
          <title>Recomendador</title>
          <RouterProvider router={router} />
        </AuthProvider>

      </HelmetProvider>
    </>
  )
}

export default App

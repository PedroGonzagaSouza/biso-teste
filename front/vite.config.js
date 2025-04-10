// import { defineConfig } from 'vite'
// import react from '@vitejs/plugin-react'
// import path from "path"
// import tailwindcss from "@tailwindcss/vite"
// // https://vite.dev/config/
// export default defineConfig({
//   plugins: [react(), tailwindcss()],
//   resolve: {
//     alias: {
//       "@": path.resolve(__dirname, "./src"),
//     },
//   },
//   optimizeDeps: {
//     exclude: ['domain'], // Exclui o módulo 'domain'
//   },
// })

import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from "path"
import tailwindcss from "@tailwindcss/vite"

export default defineConfig({
  plugins: [react(), tailwindcss()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  optimizeDeps: {
    exclude: ['domain'], // Exclui o módulo 'domain'
  },
})
import path from "path";
import React from "react";
import { createHashRouter } from "react-router-dom";
import { AppLayout } from "./pages/_layouts/app";
import { HomePage } from "./pages/home/homepage";
import { RecommendationsPage } from "./pages/teste/teste";
import { CadastroPage } from "./pages/perfil/cadastroPage";
import { LoginPage } from "./pages/perfil/loginPage";
import { ProtectedRoute } from "./protectedRoute";
// createBrowserRouter([
//     {
//         path: "/",
//         Component: Root,
//         children: [
//             { index: true, Component: Home },
//             { path: "about", Component: About },
//             {
//                 path: "auth",
//                 Component: AuthLayout,
//                 children: [
//                     { path: "login", Component: Login },
//                     { path: "register", Component: Register },
//                 ],
//             },
//         ],
//     },
// ]);

export const router = createHashRouter([
    {
        path: "/",
        element: <AppLayout />,
        children: [
            { path: "/", element: <HomePage /> },
            {
                path: "/teste", element: <ProtectedRoute> <RecommendationsPage /></ProtectedRoute>
            },
            { path: "/cadastro", element: <CadastroPage /> },
            { path: "/login", element: <LoginPage /> },

        ]
    }

])
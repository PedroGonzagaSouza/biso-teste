import path from "path";
import React from "react";
import { createBrowserRouter } from "react-router";
import { createHashRouter } from "react-router-dom";
import { AppLayout } from "./pages/_layouts/app";
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
            // { path: "/", element: <Home /> },
        ]
    }
])
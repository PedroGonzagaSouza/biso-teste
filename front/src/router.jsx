import path from "path";
import React from "react";
import { createHashRouter } from "react-router-dom";
import { AppLayout } from "./pages/_layouts/app";
import { HomePage } from "./pages/home/homepage";
import { RecomendacoesPage } from "./pages/filmes/recomendacoes/recomendacoesPage";
import { AssistidosPage } from "./pages/filmes/assistidos/AssistidosPage";
import { CadastroPage } from "./pages/perfil/cadastroPage";
import { LoginPage } from "./pages/perfil/loginPage";
import { ProtectedRoute } from "./protectedRoute";
import { FilmesPage } from "./pages/filmes/FilmesPage";

export const router = createHashRouter([
    {
        path: "/",
        element: <AppLayout />,
        children: [
            { path: "/", element: <HomePage /> },
            {
                path: "/assistidos", element: <ProtectedRoute> <AssistidosPage /></ProtectedRoute>
            },
            {
                path: "/recomendacoes", element: <ProtectedRoute> <RecomendacoesPage /></ProtectedRoute>
            },
            {
                path: "/filmes", element: <ProtectedRoute> <FilmesPage /></ProtectedRoute>
            },
            { path: "/cadastro", element: <CadastroPage /> },
            { path: "/login", element: <LoginPage /> },

        ]
    }

])
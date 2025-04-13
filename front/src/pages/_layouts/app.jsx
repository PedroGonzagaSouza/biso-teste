import { PageContainer } from "@/components/page-container"
import { Outlet } from "react-router-dom"

import { Header } from "@/components/header/Header"
export function AppLayout() {
    return (
        <div className="min-w-[calc(screen - 10px)] min-h-screen overflow-hidden antialiased font-sans bg-gray-100  dark:bg-gray-900 text-gray-900 dark:text-gray-200">
            <header className="h-15"><Header /></header>
            <div className="grid min-h-screen grid-rows-1 overflow-hidden   bg-gray-100">
                <PageContainer>
                    <Outlet />
                </PageContainer>
            </div>
            <footer className="bg-gray-800 text-white py-4">
                <div className="flex flex-row justify-center px-4 text-center">
                    <p>&copy; 2025 Movie Recommendation System. All rights reserved.</p>
                </div>
            </footer>
        </div>
    )
}
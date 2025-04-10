import { PageContainer } from "@/components/page-container"
import { Outlet } from "react-router-dom"

import { Header } from "@/components/header/Header"
export function AppLayout() {
    return (
        <div className="min-w-[calc(screen - 10px)] min-h-screen overflow-hidden antialiased font-sans">
            <header className="h-20"><Header/></header>
            <div className="grid h-full grid-rows-1 overflow-hidden">
                <PageContainer>
                    <Outlet />
                </PageContainer>
            </div>
        </div>
    )
}
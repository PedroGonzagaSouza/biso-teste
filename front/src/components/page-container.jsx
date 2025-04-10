import { twMerge } from "tailwind-merge";

export function PageContainer({ children, className }) {
    return (
        <div className={twMerge("flex flex-col h-screen min-h-screen relative ", className)}>
            {children}
        </div>
    );
}
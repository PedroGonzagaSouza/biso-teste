import { Link } from "react-router-dom";
import { twMerge } from "tailwind-merge";

export function NavbarLink({ name, className, ...props }) {
    return (
        <Link
            className={twMerge(
                "",
                className
            )}
            {...props}
        >
            {name}
        </Link>
    );
}
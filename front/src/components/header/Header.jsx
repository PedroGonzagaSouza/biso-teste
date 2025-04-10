
import { SquareUser } from "lucide-react"
import { Navbar } from "./navbar/Navbar"

export function Header() {

    return (<>
        <div className="flex flex-row justify-around p-3">
            <Navbar className="justify-center gap-20 border-0" />
            <SquareUser />
        </div>
    </>)
}
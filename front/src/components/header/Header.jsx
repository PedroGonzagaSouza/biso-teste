
import { SquareUser } from "lucide-react"
import { Navbar } from "./navbar/Navbar"

export function Header() {

    return (<>
        <div className="flex flex-row justify-between p-3">
            <div className="text-lg font-bold">Movie Recommendations</div>
            <div>
                <Navbar className="justify-center gap-20 border-0" />
            </div>
            <div>
                <SquareUser />
            </div>
        </div>
    </>)
}
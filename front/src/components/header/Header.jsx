
import { useNavigate } from "react-router-dom"
import { Navbar } from "./navbar/Navbar"
import { NavbarLink } from "./navbar/navbar-link"
import { Button } from "../ui/button"
import { useContext } from "react"
import { AuthContext } from "@/AuthContext"
export function Header() {

    const { user, logout, login } = useContext(AuthContext)
    const navigate = useNavigate()

    const handleLogout = async () => {
        await logout()
        navigate('/login')
    }

    return (<>
        <div className="flex flex-row justify-between p-3">
            <div className="text-lg font-bold">Recomendador de Filmes</div>
            <div>
                <Navbar className="justify-center gap-20 border-0" />
            </div>
            <div className="gap-10 flex items-center">
                <div className="flex items-center gap-2"><img src="https://cdn-icons-png.flaticon.com/512/149/149071.png" alt="User Avatar" className="w-10 h-10 rounded-full" />
                    {user && <span className="text-sm font-bold text-white">{user?.nome}</span>} {!user && <NavbarLink name='Entrar' to='/login' />}</div>
                {user && <Button className="bg-red-500 text-white p-1 text-sm rounded hover:bg-red-600 transition duration-200" onClick={handleLogout}> Logout</Button>}
            </div>
        </div>
    </>)
}
import {
  Menubar,
  MenubarCheckboxItem,
  MenubarContent,
  MenubarItem,
  MenubarMenu,
  MenubarRadioGroup,
  MenubarRadioItem,
  MenubarSeparator,
  MenubarShortcut,
  MenubarSub,
  MenubarSubContent,
  MenubarSubTrigger,
  MenubarTrigger,
} from "@/components/ui/menubar"
import { cn } from "@/lib/utils"
import { NavbarLink } from "./navbar-link"
export function Navbar({ className }) {

  return (
    <Menubar className={cn("", className)}>
      <NavbarLink name="Home" to="/" className="text-black-700 hover:text-black-900 dark:text-black-200 dark:hover:text-black" />
      <NavbarLink name="Recomendações" to="/recomendacoes" className="text-black-700 hover:text-black-900 dark:text-black-200 dark:hover:text-black" />

      <MenubarMenu>
        <MenubarTrigger><span className="font-sans font-bold text-md">Perfil</span></MenubarTrigger>
        <MenubarContent>
          <MenubarItem>
            <NavbarLink name="Cadastrar usuário" to="cadastro" className="text-black" />
            <NavbarLink name="login" to="login" className="text-black" />

          </MenubarItem>

        </MenubarContent>
      </MenubarMenu>

    </Menubar>
  )
}

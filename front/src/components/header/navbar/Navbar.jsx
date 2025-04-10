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
      <NavbarLink name="Teste" to="/teste" className="text-black-700 hover:text-black-900 dark:text-black-200 dark:hover:text-black" />

      <MenubarMenu>
        <MenubarTrigger><span className="font-sans font-bold text-md">Perfil</span></MenubarTrigger>
        <MenubarContent>
          <MenubarItem>
            <NavbarLink name="Cadastrar usuário" to="cadastro" className="text-black"/>
          </MenubarItem>
          <MenubarItem>
            Redo <MenubarShortcut>⇧⌘Z</MenubarShortcut>
          </MenubarItem>
          <MenubarSeparator />
          <MenubarSub>
            <MenubarSubTrigger>Find</MenubarSubTrigger>
            <MenubarSubContent>
              <MenubarItem>Search the web</MenubarItem>
              <MenubarSeparator />
              <MenubarItem>Find...</MenubarItem>
              <MenubarItem>Find Next</MenubarItem>
              <MenubarItem>Find Previous</MenubarItem>
            </MenubarSubContent>
          </MenubarSub>
          <MenubarSeparator />
          <MenubarItem>Cut</MenubarItem>
          <MenubarItem>Copy</MenubarItem>
          <MenubarItem>Paste</MenubarItem>
        </MenubarContent>
      </MenubarMenu>

    </Menubar>
  )
}

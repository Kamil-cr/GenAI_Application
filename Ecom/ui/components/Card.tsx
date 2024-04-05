"use client"
import {
CreditCard,
LogOut,
User,
} from "lucide-react"
import { Dialog } from "@/components/ui/dialog"
import { Button } from "@/components/ui/button"
import {
DropdownMenu,
DropdownMenuContent,
DropdownMenuGroup,
DropdownMenuItem,
DropdownMenuLabel,
DropdownMenuSeparator,
DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import { useRouter } from "next/navigation"
import { myDeleteCookie } from "@/lib/auth"
import { DialogDemo } from "./DialogDemo"
import Link from "next/link"
import { useState } from "react"

export function DropdownMenuDemo({name}: {name: string}) {
    const router = useRouter()
    return (
    <Dialog>
      <DropdownMenu>
        <DropdownMenuTrigger asChild>
          <Button variant="ghost">{name}</Button>
        </DropdownMenuTrigger>
        <DropdownMenuContent className="w-36 bg-inherit">
          <DropdownMenuLabel>My Account</DropdownMenuLabel>
          <DropdownMenuSeparator />
          <DropdownMenuGroup>
            {/* <DropdownMenuItem>
              <User className="mr-2 h-4 w-4" />
              <span>Edit Profile</span>
            </DropdownMenuItem> */}
            <Link href="/orders" >
            <DropdownMenuItem>
              <CreditCard className="mr-2 h-4 w-4" />
              <span>View Orders</span>
            </DropdownMenuItem>
            </Link>
          </DropdownMenuGroup>
          <DropdownMenuSeparator />
          <DropdownMenuItem onClick={() => {myDeleteCookie(); router.refresh()}}>
            <LogOut className="mr-2 h-4 w-4" />
            <span>Log out</span>
          </DropdownMenuItem>
        </DropdownMenuContent>
      </DropdownMenu>
    </Dialog>
    )
  }
  
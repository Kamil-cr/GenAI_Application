import React from 'react'
import { FaShoppingCart } from "react-icons/fa";
import Link from 'next/link';
import Search from './Search';
import { DropdownMenuDemo } from './Card';
import { cookies } from 'next/headers';
import { getUser } from "@/actions/getUser"
import { DialogDemo } from './DialogDemo';

const Navbar = async () => {
  const isCookies = cookies().has("access_token") || cookies().has("refresh_token");  
  const user = await getUser()
  const name: string = user.username
  const email: string = user.email
  return (
    <nav className='pointer-events-auto w-full lg:px-0 px-3.5 gap-4 xs:px-6 sm:px-12 py-6 flex items-center justify-center border-zinc-800 border-b border-solid'>
        <ul className='flex justify-between gap-2 text-sm'>
          <li className='flex px-3 items-center justify-center '>
            <Link className='text-md py-3 px-3 rounded-md transition-all text-[#EDEDED] hover:bg-[#1F1F1F] relative' href={`/`}>Home</Link>
          </li>
        </ul>
        <div className='w-1/2 mx-5'>
          <Search />
        </div>
        <ul className='flex space-x-3 justify-center'>
          <li className='flex px-3 items-center justify-center '>
            <Link className='text-lg py-3 px-3 rounded-md transition-all text-[#EDEDED] hover:bg-[#1F1F1F] relative' href={`/cart`}><FaShoppingCart /></Link>
          </li>
          {isCookies ? 
          <DropdownMenuDemo name={name}/> :
          <li className='flex px-3 items-center justify-center '>
            <Link className='text-md py-3 px-3 rounded-md transition-all text-[#EDEDED] hover:bg-[#1F1F1F] relative' href={`/login`}>Login</Link>
          </li>}
        </ul>
        {isCookies ? <DialogDemo name={name} email={email} />: null}
    </nav>
  )
}

export default Navbar
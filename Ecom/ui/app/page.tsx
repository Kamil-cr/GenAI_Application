import Products from "@/components/Products";
import { cookies } from "next/headers";

interface Props {
  searchParams: {
    search: string
  }
}

export default async function Home({searchParams}: Props) {    
  const isCookies = cookies().has("access_token");
  console.log(isCookies, "isCookies");
  
  return (
    <main className="flex justify-center">
      <Products search={searchParams.search}/>
    </main>
  );}


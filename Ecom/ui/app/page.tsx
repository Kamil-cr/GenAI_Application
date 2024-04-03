import Products from "@/components/Products";
import {token, myGetCookie} from "@/lib/auth";

interface Props {
  searchParams: {
    search: string
  }
}

export default async function Home({searchParams}: Props) {  
  const pa = await token()
  const fa = await myGetCookie()
  console.log(pa, "data");
  console.log(fa, "data");
  
  return (
    <main className="flex justify-center">
      <Products search={searchParams.search}/>
    </main>
  );
}

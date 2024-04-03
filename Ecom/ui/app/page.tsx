import Products from "@/components/Products";

interface Props {
  searchParams: {
    search: string
  }
}

export default async function Home({searchParams}: Props) {    
  return (
    <main className="flex justify-center">
      <Products search={searchParams.search}/>
    </main>
  );}


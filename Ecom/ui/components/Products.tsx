import Link from "next/link"
import Image from "next/image"
import { products } from "@/actions/products"

interface Iprops {
    search?: string
}

export interface IProducts {
    name: string,
    price: number,
    image1: string,
    image2: string,
    description: string,
    slug: string,
    sku: string
}

const Products = async ({search}: Iprops) => {    
    const data: IProducts[] = await products(search)
    return (
      <div className='lg:mx-20 md:mx-10 grid lg:grid-cols-3 xl:grid-cols-4 md:grid-cols-2 grid-cols-1 md:space-y-6 space-y-9 space-x-5 md:space-x-10 '>
        {data.map((product, index) => {
            const images = [product.image1, product.image2]
            return (
                <div key={index} className='flex md:mt-6 md:ml-10 mt-9 ml-6 justify-between border border-solid border-zinc-800 rounded-md flex-col'>
                    <Link href={`/products/${product.slug}`}>
                        <div className='overflow-hidden'>
                        <Image src={images[0]} alt={product.name} className='transition-transform duration-500 ease-in-out transform hover:scale-110' width={300} height={425} />
                        </div> 
                        <div className='flex justify-between relative flex-col gap-2.5 p-3.5 z-10'>
                            <h3 className='font-semibold text-sm line-clamp-1'>{product.name}</h3>
                            <p className='text-gray-500 text-sm mt-1'>${product.price}</p>
                        </div>
                    </Link>
                </div>
            )
        })}
      </div>
    )
}

export default Products
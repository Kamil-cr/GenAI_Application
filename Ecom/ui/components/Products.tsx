import { productfetch} from "@/actions/product-fetch"
import Link from "next/link"
import Image from "next/image"
import { IProducts } from "@/app/products/[slug]/page"

const Products = async () => {
    const products: IProducts[] = await productfetch()
    return (
      <div className='lg:mx-20 md:mx-10 grid lg:grid-cols-3 xl:grid-cols-4 md:grid-cols-2 w-max grid-cols-1 md:space-y-6 space-y-9 space-x-5 md:space-x-10 '>
        {products.map((product, index) => {
            const images = [product.image_1, product.image_2]
            return (
                <div key={index} className='flex md:mt-6 md:ml-10 mt-9 ml-6 justify-between border border-solid border-zinc-800 rounded-md flex-col'>
                    <Link href={`/products/${product.slug}`}>
                        <div className='overflow-hidden'>
                        <Image src={images[0]} alt={product.name} className='transition-transform duration-500 ease-in-out transform hover:scale-110' width={300} height={425} />
                        </div>
                        <div className='flex justify-between flex-col gap-2.5 p-3.5 z-10'>
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
import { GetCart } from '@/actions/get_cart_product'
import Link from 'next/link'
import Image from 'next/image'
import { IProducts } from '@/components/Products'
import ProductQuantity from '@/components/ProductQuantity'

export interface ICart {
  product_id: string,
  product_size: string,
  quantity: number,
  user_id: string,
  id: number,
  product_total: number,
  product_data: IProducts
}

const page = async () => {
  const data: ICart[] = await GetCart() || []
  const price = data.reduce((acc, product) => acc + product.product_data.price*product.quantity, 0)
    return (
      <div className='lg:mx-20 md:mx-10 grid lg:grid-cols-3  md:grid-cols-2 grid-cols-1 md:space-y-6 space-y-9 space-x-5 md:space-x-10 '>
        {data.map((product, index) => {    
            const images = [product.product_data.image1, product.product_data.image2]
            return (
                <div key={product.product_data.sku} className='flex md:mt-6 md:ml-10 mt-9 ml-6 justify-between border border-solid border-zinc-800 rounded-md flex-col'>
                    <Link href={`/products/${product.product_data.slug}`}>
                        <div className='overflow-hidden'>
                        <Image src={images[0]} alt={product.product_data.name} className='transition-transform duration-500 ease-in-out transform hover:scale-110' width={384} height={576} />
                        </div> 
                        <div className='flex justify-between relative flex-col gap-2.5 p-3.5 z-10'>
                            <h3 className='font-semibold text-sm line-clamp-1'>{product.product_data.name}</h3>
                            <p className='text-gray-500 text-sm mt-1'>${(product.product_data.price*product.quantity).toFixed(2)}</p>
                        </div>
                    </Link>
                    <ProductQuantity {...product} />
                </div>
            )
        })}
        <div className='fixed left-[50%] translate-x-[-50%] bottom-4 w-[90%] z-10 sm:w-[360px] rounded-xl overflow-hidden flex bg-black border border-solid border-border-primary h-min'>
          <div className="flex flex-col p-2.5 justify-center w-1/2 gap-2 text-center">
            <div className='flex gap-2.5 justify-center text-sm'>
              <span>Total:</span>
              <span>{price}</span>
            </div>
              <span className='text-xs'>+ TAX INCL.</span>
          </div>
          <div className='w-1/2 border-l border-solid bg-background-secondary border-border-primary'>
            <button className='w-full h-full text-white bg-button-primary'>
              <Link href={"/"}>Checkout</Link>
            </button>
          </div>
        </div>
      </div>
    )
}

export default page
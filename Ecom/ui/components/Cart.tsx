import React from 'react'
import { GetServerSideProps } from 'next';
import { IProducts } from './Products';
import { GetCart } from '@/actions/get_cart_product';
import { getProductbyID } from '@/actions/getProduct';
import Link from 'next/link';
import Image from 'next/image';
import { ICart } from '@/app/cart/page';
// ...

export const getServerSideProps: GetServerSideProps = async () => {
  const data: ICart[] = await GetCart();
  const products = await Promise.all(data.map(product => getProductbyID(product.product_id)));
  return { props: { products } };
};

const Cart = ({ products }: { products: ICart[] }) => {
    <div className='lg:mx-20 md:mx-10 grid lg:grid-cols-3 xl:grid-cols-4 md:grid-cols-2 grid-cols-1 md:space-y-6 space-y-9 space-x-5 md:space-x-10 '>
        {products.map(async (prod, index) => {    
            const product: IProducts = await getProductbyID(prod.product_id)    
            const images = [product.image1, product.image2]
            return (
                <div key={index} className='flex md:mt-6 md:ml-10 mt-9 ml-6 justify-between border border-solid border-zinc-800 rounded-md flex-col'>
                    <Link href={`/products/${product.slug}`}>
                        <div className='overflow-hidden'>
                        <Image src={images[0]} alt={product.name} className='transition-transform duration-500 ease-in-out transform hover:scale-110' width={384} height={576} />
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
}


export default Cart
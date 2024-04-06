import { GetCart } from '@/actions/get_cart_product'
import React from 'react'

const page = () => {
  GetCart()
  return (
    <div className='h-full'></div>
  )
}

export default page
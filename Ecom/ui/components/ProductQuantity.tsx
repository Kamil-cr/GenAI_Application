"use client"
import { ICart } from '@/app/cart/page'
import React from 'react'
import { useState } from 'react'

const ProductQuantity = (product_quantity: ICart) => {
    let [quantity, setQuantity] = useState(product_quantity.quantity)
  return (
    <div className='flex bg-black w-min'>
        <button onClick={() => setQuantity(quantity--)} className='flex items-center justify-center w-8 h-8 p-2 border border-solid rounded-l border-border-primary '>-</button>
        <span className='flex items-center justify-center w-8 h-8 p-2 border border-solid border-border-primary'>{quantity}</span>
        <button onClick={()=> setQuantity(quantity++)} className='flex items-center justify-center w-8 h-8 p-2 border border-solid rounded-r border-border-primary'>+</button>
    </div>
  )
}

export default ProductQuantity
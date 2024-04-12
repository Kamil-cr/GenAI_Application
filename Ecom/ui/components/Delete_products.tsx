"use client"
import { deleteCart } from "@/actions/delete_cart"
import { useRouter } from "next/navigation"

interface IDelete_products {
    product_id: string,
    product_size: string,
    quantity: number
}

const Delete_products = ({product_id, product_size, quantity}: IDelete_products) => {
    const router = useRouter()
  return (
        <span onClick={() => {deleteCart(product_id, product_size, quantity); router.refresh()}} className='text-gray-500 text-lg cursor-pointer' >x</span>
  )
}

export default Delete_products
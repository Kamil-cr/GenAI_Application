"use server"
import { cookies } from "next/headers"

export async function deleteCart(product_id: string, product_size: string, quantity: number) {
    const isCookies = cookies().get("access_token")?.value
  const res = await fetch(`http://localhost:3000/api/cart`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${isCookies}`
    },
    body: JSON.stringify({product_id, product_size, quantity})
  })
  return res.json()
}
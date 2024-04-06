"use server"
import { IProducts } from "@/components/Products"
import { cookies } from "next/headers";

export const addToCart = async (size: string, product_data: IProducts) => {
    const isCookies = cookies().get("access_token")?.value;
    try{
        const response = await fetch(`${process.env.NEXT_PUBLIC_BASE_URL}/api/cart`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                'Authorization': `Bearer ${isCookies}`
            },
            body: JSON.stringify({
                product_id: product_data.sku,
                quantity: 1,
                product_size: size
            }),
        })
        const data = await response.json()
        console.log(data, "data");
        
        return data
    } catch (error) {
        console.log(error, "error");
        console.log("error is error");
    }
}
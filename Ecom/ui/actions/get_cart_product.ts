"use server"
import { cookies } from "next/headers";
import { getProductbyID } from "./getProduct";

export const GetCart = async () => {
    const isCookies = cookies().get("access_token")?.value;
    try{
        const response = await fetch(`${process.env.NEXT_PUBLIC_BASE_URL}/api/cart`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                'Authorization': `Bearer ${isCookies}`
            },
        })
        const data = await response.json()
        const product = await Promise.all(data.map(async (prod: any) => {
            const product_data = await getProductbyID(prod.product_id)
            return {...prod, product_data}
        }))
        return product
    } catch (error) {
        console.log(error, "error");
        console.log("error is error");
    }
}
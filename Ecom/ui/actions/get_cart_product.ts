"use server"
import { cookies } from "next/headers";

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
        return data
    } catch (error) {
        console.log(error, "error");
        console.log("error is error");
    }
}
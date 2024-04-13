"use server"
import { cookies } from "next/headers"

interface IData {
    prod: {
    firstname: string,
    lastname: string,
    address: string,
    state: string,
    city: string,
    contactnumber: string
    }
}

export const placeorder = async ({prod}: IData) => {
    const isCookies = cookies().get("access_token")?.value
    try{
        const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/order`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${isCookies}`
            },
            // body: JSON.stringify(prod)
        })
        console.log(prod, "Parci");
        const data = await response.json()
        return data
        
    }
    catch(err){
        return err
    }
}
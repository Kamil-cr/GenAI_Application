"use server"
import { cookies } from "next/headers"

interface IData {
    user: {
    firstname: string,
    lastname: string,
    address: string,
    state: string,
    city: string,
    contactnumber: string,
    paymentmethod: string
    }
}

export const placeorder = async (firstname: string, lastname: string, address: string, state: string,city: string,contactnumber: string, paymentmethod: string) => {
    const isCookies = cookies().get("access_token")?.value
    try{
        const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/order`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${isCookies}`
            },
            body: JSON.stringify(
                {
                    firstname: firstname,
                    lastname: lastname,
                    address: address,
                    state: state,
                    city: city,
                    contactnumber: contactnumber,
                    payment_method: paymentmethod
                }
            )
        })
        const data = await response.json()
        return data
        
    }
    catch(err){
        return err
    }
}
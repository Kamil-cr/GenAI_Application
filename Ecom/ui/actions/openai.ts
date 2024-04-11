"use server"
import { cookies } from "next/headers";

export const openaiapi = async (prompt: string) => {
    // console.log(prompt, "prompt");    
    // const isCookies = cookies().get("access_token")?.value;
    try {
        const response = await fetch(`${process.env.NEXT_PUBLIC_BASE_URL}/api/openai?prompt=${prompt}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
        })
        const data = await response.json()    
        return data.message
    } catch (error) {
        console.log(error, "error");
        console.log("error is error");
    }
}
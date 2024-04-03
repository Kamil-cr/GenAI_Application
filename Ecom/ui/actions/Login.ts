"use server"
import { mySetCookie } from "@/lib/auth"
import { useRouter } from "next/navigation"

export const sign = async (username: string, password:string) => {
    const formData = new URLSearchParams();
    formData.append('username', username);
    formData.append('password', password);
  try {
      const res = await fetch(`http://localhost:3000/api/oauth/login`, {
          method: 'POST',
          headers: {
              'Content-Type': 'application/x-www-form-urlencoded',
          },
          body: formData
      })

      const data = await res.json()
      if (data && data.access_token && data.refresh_token) {
        await mySetCookie(data.access_token, data.refresh_token)
      }
      console.log(data);
      return data
  }
  catch (error) {
      console.log(error, "error");
      console.log("error is error");
  }
}
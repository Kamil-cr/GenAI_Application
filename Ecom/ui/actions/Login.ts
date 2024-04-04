"use server"
import { mySetCookie } from "@/lib/auth"
import { useRouter } from "next/navigation"
import { cookies } from "next/headers"

export const loginUser = async (username: string, password:string) => {
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
        cookies().set({
            name: 'access_token',
            value: data.access_token,
            httpOnly: true,
            path: '/',
            expires: new Date(Date.now() + 60 * 60 * 1000)
          })
            cookies().set({
                name: 'refresh_token',
                value: data.refresh_token,
                httpOnly: true,
                path: '/',
                expires: new Date(Date.now() + 60 * 60 * 1000 * 24 * 7)
            })
      }
      return data
  }
  catch (error) {
      console.log(error, "error");
      console.log("error is error");
  }
}
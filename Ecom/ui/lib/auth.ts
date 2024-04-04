"use server";
// import { getCookies, setCookie, deleteCookie, getCookie, hasCookie } from 'cookies-next';
import { cookies } from 'next/headers';
// export const myGetCookie = async () => {
//     return getCookies()
// }

// export const mySetCookie = async (token: string, refresh_token: string) => {
//     const now = new Date();
//     const expirationTime = new Date(now.getTime() + 60 * 60 * 1000)
//     if (hasCookie("access_token")) {
//         console.log("token exist");
//     } else {
//         setCookie("access_token", token, { expires: expirationTime })
//         setCookie("refresh_token", refresh_token, { expires: expirationTime })
//     }
// }

export const myDeleteCookie = () => {
    cookies().delete("access_token") 
    cookies().delete("refresh_token")
    console.log("cookie deleted");
}

// export async function auth() {
//   // Check if cookies exist
//   const isCookies = cookies().has("access_token");

//   if (!isCookies) {
//     console.log("[auth] No cookies. Redirecting to login.");
//     return null;
//   }

//   const cookies_user_data = cookies().get("access_token")?.value;

//   if (!cookies_user_data) {
//     console.log("[auth] No user data in cookies. Redirecting to login.");
//     return null;
//   }

//   let user_data: UserData = JSON.parse(cookies_user_data);
//   console.log("[auth] user_data CALLED @auth");

//   if (!user_data.access_token) {
//     console.log("[auth] Expired Redirecting to login.");
//     return null;
//   }

//   return user_data;
// }

// export async function token() {
//     const isCookies = cookies().has("access_token");
//     const cookies_user_data = cookies().get("refresh_token");
//     return {isCookies, cookies_user_data};
// } 

"use server"

export const registerUser = async (username: string, email: string, password: string) => {
    try{
    const response = await fetch("http://localhost:8000/api/signup", {
        method: "POST",
        headers: {
        "Content-Type": "application/json",
        },
        body: JSON.stringify({
        username: username,
        email: email,
        hashed_password: password,
        }),
    })
    const data = await response.json()
    return {"message": "User registered successfully"}
    } catch (error) {
        console.log(error, "error");
        console.log("error is error");
    }
}
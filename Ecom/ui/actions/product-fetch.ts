import axios from "axios"

export async function productfetch () {
    const response = await fetch('http://localhost:3000/api/products', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    const data = await response.json()
    return data
}
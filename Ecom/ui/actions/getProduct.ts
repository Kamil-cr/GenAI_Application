"use server"
export const getProducts = async(name: string) => {
      try {
          const res = await fetch(`http://localhost:3000/api/products/${name}`, {
              method: 'GET',
              headers: {
                'Content-Type': 'application/json'
              },
          })
          const data = await res.json()
          return data
      }
      catch (error) {
          console.log(error, "error");
          console.log("error is error");
      }
}
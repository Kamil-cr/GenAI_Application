"use server"
export const getProducts = async(name: string) => {
      try {
          const res = await fetch(`${process.env.NEXT_PUBLIC_BASE_URL}/api/products/${name}`, {
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
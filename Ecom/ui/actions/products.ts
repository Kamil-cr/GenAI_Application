"use server"
export const products = async(search?: string) => {
// const formData = new URLSearchParams();
//     formData.append('search', search? search : '');
  try {
      const res = await fetch(`${process.env.NEXT_PUBLIC_BASE_URL}/api/products${search? `?query=${search}`: ""}`, {
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
const getTodo = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/api/", {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        },
        cache: "force-cache"
        }
        );
        const data = await response.json();
        console.log(data);
        return data;
    } catch (error) {
        console.error(error);
        return null;
    }
}

// // const postTodo = async (todo: string) => {
// //     try {
// //         const response = await fetch("http://localhost:3000/api/todos", {
// //         method: "POST",
// //         headers: {
// //             "Content-Type": "application/json"
// //         },
// //         body: JSON.stringify(
// //             { todo })
// //         });
// //         if (!response.ok) {
// //         throw new Error("Failed to fetch data");
// //         }
// //         const data = await response.json();
// //         console.log(data);
// //         return data;
// //     } catch (error) {
// //         console.error(error);
// //         return null;
// //     }
// // }

// export const deleteTodo = async (title: string) => {
//     try {
//         const response = await fetch(`http://localhost:3000/api/todos`, {
//         method: "DELETE",
//         headers: {
//             "Content-Type": "application/json"
//         },
//         body: JSON.stringify(
//             {"title": title })
//         });
//         const data = await response.json();
//         console.log(data);
//         return data;
//     } catch (error) {
//         console.error(error);
//         return null;
//     }
// }
export default getTodo
"use client"
// import getTodo from "@/utils/Todo";
import { FaEdit } from "react-icons/fa";
import { MdDelete } from "react-icons/md";
import { useRouter } from "next/navigation";
import getTodo from "@/utils/Todo";

export default async function Home() {
  // const todo = await getTodo();
  const router = useRouter();
  console.log(getTodo());
  
  return (
    <main className="max-w-screen-sm flex justify-center self-center flex-col mx-auto my-28">
      <h2 className="text-2xl font-bold justify-center flex self-center">Todo List</h2>
      <div className="flex justify-center my-4">
        <input
          type="text"
          placeholder="Search Todo"
          className="border border-gray-300 w-full rounded-md px-4 py-2"
          onChange={(e) => router.push(`/?search=${e.target.value}`)}
        />
        <button className="ml-2 bg-blue-500 text-white px-4 py-2 rounded-md">
          Search
        </button>
      </div>
      <div className="bg-red-300 px-5 text-xl flex justify-between text-red-100">
      {/* {
      todo.map((todo: Todo) => {
        return(
        <div key={todo.id}>
          <div>{todo.title}</div>
        </div>
  )})
      } */}
      <div className="flex self-center space-x-2">
        <FaEdit />
        <MdDelete />
      </div>
      </div>
    </main>
  );
  }
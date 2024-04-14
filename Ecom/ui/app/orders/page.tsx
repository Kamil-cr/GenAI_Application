import { userOrders } from "@/actions/getOrder"
import {
    Table,
    TableBody,
    TableCaption,
    TableCell,
    TableFooter,
    TableHead,
    TableHeader,
    TableRow,
} from "@/components/ui/table"

interface IOrders {
    id: number;
    first_name: string;
    last_name: string;
    address: string;
    city: string;
    state: string;
    contact_number: string;
    payment_method: string;
    order_date: string;
    order_total: number;
    order_status: string;
    user_id: string;
}  

const TableDemo = async () => {
    const orders: IOrders[] = await userOrders()
    const totalAmount = orders.reduce((acc, order) => acc + order.order_total, 0)

    if(orders){
        return(
    <Table>
        <TableCaption>A list of your recent orders.</TableCaption>
        <TableHeader>
            <TableRow>
            <TableHead className="w-[100px]">Orders</TableHead>
            <TableHead>First Name</TableHead>
            <TableHead>Last Name</TableHead>
            <TableHead>Status</TableHead>
            <TableHead>Method</TableHead>
            <TableHead>Address</TableHead>
            <TableHead className="text-right">Amount</TableHead>
            </TableRow>
        </TableHeader>
        <TableBody>
            {orders.map((order) => (
            <TableRow key={order.id}>
                <TableCell className="font-medium">{order.id}</TableCell>
                <TableCell>{order.first_name}</TableCell>
                <TableCell>{order.last_name}</TableCell>
                <TableCell>{order. order_status}</TableCell>
                <TableCell>{order.payment_method}</TableCell>
                <TableCell>{order.address}, {order.city}, {order.state}</TableCell>
                <TableCell className="text-right">{order.order_total}</TableCell>
            </TableRow>
            ))}
        </TableBody>
        <TableFooter>
            <TableRow>
            <TableCell colSpan={7}>Total</TableCell>
            <TableCell className="text-right">{totalAmount}</TableCell>
            </TableRow>
        </TableFooter>
    </Table>
    )} else {
        return <div>no order found</div>
    }
}

export default TableDemo
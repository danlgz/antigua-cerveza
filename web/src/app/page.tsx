import { listBeers } from "@/actions/list-beers";
import { listOrders } from "@/actions/list-orders";
import OrderCard from "@/components/order-card";

export default async function Page() {
  const orders = await listOrders();
  await new Promise(resolve => setTimeout(resolve, 2000)) // test skeleton

  return (
    <div className="flex flex-col gap-4 ">
      {
        orders.map(i => <OrderCard key={i.id} items={i.items} rounds={i.rounds} total={i.total} />)
      }
    </div>
  );
}

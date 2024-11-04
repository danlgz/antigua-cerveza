import listBeersStock from "@/actions/list-beers-stock";
import retrieveOrder from "@/actions/retrieve-order"
import OrderDetailCard from "@/components/order-detail-card";
import { notFound } from "next/navigation"

export default async function Page({ params: { id } }: { params: { id: string } }) {
  const { ok, data: order } = await retrieveOrder(id)
  if (!ok || !order) return notFound();

  const { data: beers } = await listBeersStock(order.items.map(i => i.beerStockId));
  if (beers === undefined) return notFound();

  return (
    <OrderDetailCard order={order} beers={beers} />
  )
}

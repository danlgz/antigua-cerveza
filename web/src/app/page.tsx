import listBeersStock from "@/actions/list-beers-stock";
import listOrders from "@/actions/list-orders";
import OrderCard from "@/components/order-card";
import { BeerStock } from "@/types/beer-stock";
import { Order } from "@/types/order";

function ImplementedOrderCar({ order, beerImageNames }: { order: Order, beerImageNames: string[] }) {
  const totalBeers = order.rounds.map(r => r.items.map(i => i.quantity)).flat().reduce((p, c) => p + c, 0);

  return (
    <OrderCard
      key={order.id}
      beersCount={totalBeers}
      roundsCount={order.rounds.length}
      total={order.total}
      beerImageNames={beerImageNames}
      isPaid={order.paid}
      href={`/order/${order.id}`}
    />
  )
}

export default async function Page() {
  // await new Promise(resolve => setTimeout(resolve, 2000)) // test skeleton

  const { data } = await listOrders();
  const orders = data || [];

  const beersByOrder = orders.reduce((prev, current) => {
    prev[current.id] = current.items.map(e => e.beerStockId);
    return prev;
  }, {} as Record<string, string[]>);

  const { data: beers } = await listBeersStock(Object.values(beersByOrder).flat());
  const beersById = (beers || []).reduce((prev, beer) => {
    prev[beer.id] = beer;
    return prev;
  }, {} as Record<string, BeerStock>)

  return (
    <div className="flex flex-col gap-4 ">
      {
        orders.map(
          order => (
            <ImplementedOrderCar
              key={order.id}
              order={order}
              beerImageNames={beersByOrder[order.id].map(beerId => beersById[beerId].img)}
            />
          )
        )
      }
    </div>
  );
}

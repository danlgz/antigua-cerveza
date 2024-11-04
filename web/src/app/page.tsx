import listBeersStock from "@/actions/list-beers-stock";
import listOrders from "@/actions/list-orders";
import OrderCard from "@/components/order-card";
import { BeerStock } from "@/types/beer-stock";

export default async function Page() {
  const orders = await listOrders();
  // await new Promise(resolve => setTimeout(resolve, 2000)) // test skeleton

  const beersByOrder = orders.reduce((prev, current) => {
    prev[current.id] = current.items.map(e => e.beerStockId);
    return prev;
  }, {} as Record<string, string[]>);

  const beers = await listBeersStock(Object.values(beersByOrder).flat());
  const beersById = beers.reduce((prev, beer) => {
    prev[beer.id] = beer;
    return prev;
  }, {} as Record<string, BeerStock>)

  return (
    <div className="flex flex-col gap-4 ">
      {
        orders.map(
          order => {
            const totalBeers = order.rounds.map(r => r.items.map(i => i.quantity)).flat().reduce((p, c) => p + c, 0);

            return (
              <OrderCard
                key={order.id}
                beersCount={totalBeers}
                roundsCount={order.rounds.length}
                total={order.total}
                beerImageNames={beersByOrder[order.id].map(beerId => beersById[beerId].img)}
                isPaid={order.paid}
              />
            )
          }
        )
      }
    </div>
  );
}

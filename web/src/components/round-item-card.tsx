import { BeerStock } from "@/types/beer-stock";
import { OrderRound } from "@/types/order"
import BeerImage from "./beer-image";
import { Card, CardContent } from "./ui/card";

const USDollar = new Intl.NumberFormat('en-US', {
  style: 'currency',
  currency: 'USD',
});

type Props = {
  round: OrderRound;
  beersById: Record<string, BeerStock>;
  ordinal: number;
}

export default function RoundItemCard({ round, beersById, ordinal }: Props) {
  const rountTotal = round.items.map(ri => ri.quantity * beersById[ri.beerStockId].price).reduce((p, c) => p + c, 0)
  const beersTotal = round.items.reduce((p, c) => p + c.quantity, 0)
  return (
    <Card className="w-full flex items-center shadow-none">
      <CardContent className="flex justify-between items-end py-4 px-8 w-full">
        <div>
          <h3 className="font-bold mb-0 flex">Round {ordinal}</h3>
          <p className="mb-3 text-sm opacity-50">Beers: {beersTotal}</p>
          <div className="flex flex-col gap-2">
            {
              round.items.map((ri, i) => {
                const beer = beersById[ri.beerStockId];
                return (
                  <div key={i} className="flex gap-2">
                    <BeerImage imgName={beer.img} className="h-10 w-auto" />
                    <div>
                      <h4 className="text-sm font-semibold">{beer.name}</h4>
                      <p className="text-xs opacity-50">Quantity: {ri.quantity}</p>
                    </div>
                  </div>
                )
              })
            }
          </div>
        </div>
        <div>
          <p className="text-right opacity-50 text-sm">Total:</p>
          <h2 className="text-3xl font-bold">{USDollar.format(rountTotal)}</h2>
        </div>
      </CardContent>
    </Card>
  )
}

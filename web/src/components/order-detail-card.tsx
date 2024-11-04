import { Order } from "@/types/order";
import { Button } from "./ui/button";
import { Card, CardContent, CardFooter } from "./ui/card";
import { cn } from "@/lib/utils";
import Link from "next/link";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { BeerStock } from "@/types/beer-stock";
import OrderItemCard from "./order-item-card";
import BeerImage from "./beer-image";
import RoundItemCard from "./round-item-card";

const USDollar = new Intl.NumberFormat('en-US', {
  style: 'currency',
  currency: 'USD',
});


type Props = {
  order: Order;
  beers: BeerStock[];
}

export default function OrderDetailCard({ order: { total, rounds, items, paid, subtotal, discounts, taxes }, beers }: Props) {
  const beersById = (beers || []).reduce((prev, beer) => {
    prev[beer.id] = beer;
    return prev;
  }, {} as Record<string, BeerStock>)

  return (
    <Card className="w-full">
      <CardContent className="flex flex-col items-top pt-8 gap-8">
        <div className="flex flex-col items-center gap-4">
          <p className="text-sm font-medium text-center">Order #1234</p>
          <h1 className="text-5xl font-bold">${total}</h1>

          <div className="flex gap-3 justify-center">
            <p className="text-xs text-muted-foreground">
              Total Beers: {items.length}
            </p>
            <p className="text-xs text-muted-foreground">
              Total Rounds: {rounds.length}
            </p>
          </div>

          <span className={cn("py-1 px-4 rounded-full bg-red-200 text-black", paid ? "bg-green-200" : "bg-red-200")}>
            {paid ? "Paid" : "Unpaid"}
          </span>
        </div>

        <div className="flex justify-center">
          <Tabs defaultValue="rounds" className="flex flex-col items-center w-full">
            <TabsList className="mb-4">
              <TabsTrigger value="beers" className="px-10">Beers</TabsTrigger>
              <TabsTrigger value="rounds" className="px-10">Rounds</TabsTrigger>
            </TabsList>
            <TabsContent value="beers" className="w-full flex flex-col gap-4">
              {
                items.map(item => {
                  const beer = beersById[item.beerStockId];
                  return <OrderItemCard key={item.beerStockId} item={item} beer={beer} />
                })
              }
            </TabsContent>
            <TabsContent value="rounds" className="w-full flex flex-col gap-4">
              {
                rounds.map((round, i) => (
                  <RoundItemCard key={i} round={round} beersById={beersById} ordinal={i + 1} />
                ))
              }
            </TabsContent>
          </Tabs>
        </div>
      </CardContent>
      <CardFooter className="flex flex-col justify-center mb-2 mt-4 items-center">
        <div className="w-full text-right text-sm">
          <p className="bg-opacity-50">Subtotal: {USDollar.format(subtotal)}</p>
          <p className="bg-opacity-50">Taxes: {USDollar.format(taxes)}</p>
          <p className="bg-opacity-50">Discounts: {USDollar.format(discounts)}</p>
          <h3 className="font-bold text-base my-2">Total: {USDollar.format(total)}</h3>
        </div>
        <Link href="/">
          <Button variant="outline">Go back</Button>
        </Link>
      </CardFooter>
    </Card>
  )
}

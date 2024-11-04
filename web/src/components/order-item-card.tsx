import { BeerStock } from "@/types/beer-stock";
import { OrderItem } from "@/types/order";
import { Card, CardContent } from "./ui/card";
import BeerImage from "./beer-image";

type Props = {
  item: OrderItem;
  beer: BeerStock;
}

export default function OrderItemCard({ item, beer }: Props) {

  return (
    <Card className="w-full flex items-center shadow-none">
      <CardContent className="flex justify-between items-center py-4 px-8 w-full">
        <div className="flex gap-4 items-center">
          <BeerImage imgName={beer.img} />
          <div>
            <h3 className="text-xl font-bold mb-1">{beer.name}</h3>
            <p className="opacity-50 text-sm">Quantity: {item.quantity}</p>
            <p className="opacity-50 text-sm">Unit price: ${beer.price}</p>
          </div>
        </div>
        <div>
          <p className="text-right opacity-50 text-sm">Total:</p>
          <h2 className="text-3xl font-bold">${item.total}</h2>
        </div>
      </CardContent>
    </Card>
  )
}

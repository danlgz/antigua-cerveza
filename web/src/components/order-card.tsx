import { cn } from "@/lib/utils";
import BeerImage from "./beer-image";
import { Avatar } from "./ui/avatar";
import { Button } from "./ui/button";
import { Card, CardContent, CardFooter } from "./ui/card";
import Link from "next/link";

function BeerAvatar({ imgName }: { imgName: string }) {
  return (
    <Avatar className="h-auto w-9">
      <BeerImage imgName={imgName} />
    </Avatar>
  )
}


type Props = {
  total: number;
  roundsCount: number;
  beersCount: number;
  beerImageNames: string[];
  isPaid: boolean;
  href: string;
}

export default function OrderCard({ total, roundsCount, beersCount, beerImageNames, isPaid, href }: Props) {
  return (
    <Card className="w-full">
      <CardContent className="flex justify-between items-top pt-8">
        <div>
          <p className="text-sm font-medium mb-2">Order #1234</p>
          <h1 className="text-4xl font-bold mb-2">${total}</h1>
          <p className="text-xs text-muted-foreground">
            Total Rounds: {roundsCount}
          </p>
          <p className="text-xs text-muted-foreground">
            Total Beers: {beersCount}
          </p>
        </div>
        <div>
          <h3 className="text-sm font-medium mb-2 text-right">Requested Beers:</h3>
          <div className="flex overflow-hidden justify-end gap-1">
            {
              beerImageNames.map(imgName => <BeerAvatar key={imgName} imgName={imgName} />)
            }
          </div>
        </div>
      </CardContent>
      <CardFooter className="flex justify-between mb-2 items-center">
        <span className={cn("py-1 px-4 rounded-full bg-red-200 text-black", isPaid ? "bg-green-200" : "bg-red-200")}>
          {isPaid ? "Paid" : "Unpaid"}
        </span>
        <Link href={href}>
          <Button variant="outline">View Details</Button>
        </Link>
      </CardFooter>
    </Card>
  )
}

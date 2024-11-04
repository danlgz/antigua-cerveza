import BeerImage from "./beer-image";
import { Avatar } from "./ui/avatar";
import { Button } from "./ui/button";
import { Card, CardContent, CardFooter } from "./ui/card";

function BeerAvatar({ imgName }: { imgName: string }) {
  return (
    <Avatar className="h-auto w-9">
      <BeerImage imgName={imgName} />
    </Avatar>
  )
}

export default function OrderCard() {
  return (
    <Card className="w-full">
      <CardContent className="flex justify-between items-top pt-8">
        <div>
          <p className="text-sm font-medium mb-2">Order #1234</p>
          <h1 className="text-4xl font-bold mb-2">$50.00</h1>
          <p className="text-xs text-muted-foreground">
            Total Rounds: 10
          </p>
          <p className="text-xs text-muted-foreground">
            Total Beers: 15
          </p>
        </div>
        <div>
          <h3 className="text-sm font-medium mb-2 text-right">Requested Beers:</h3>
          <div className="flex overflow-hidden justify-end gap-1">
            <BeerAvatar imgName="sin-novia" />
            <BeerAvatar imgName="muy-noble" />
            <BeerAvatar imgName="don-nadie" />
            <BeerAvatar imgName="cucurucho" />
          </div>
        </div>
      </CardContent>
      <CardFooter className="flex justify-end mb-2">
        <Button variant="outline">View Details</Button>
      </CardFooter>
    </Card>
  )
}

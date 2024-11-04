import { Button } from "@/components/ui/button"
import { Card, CardContent, CardFooter } from "@/components/ui/card"
import Link from "next/link"
import { BeerOff } from "lucide-react"

export default function OrderNotFound() {
  return (
    <Card className="w-full">
      <CardContent className="flex flex-col items-center justify-center pt-8 gap-6 h-[500px]">
        <div className="bg-background p-8 rounded-full">
          <BeerOff className="w-16 h-16" />
        </div>
        <div className="text-center">
          <h1 className="text-2xl font-bold mb-2">Order Not Found</h1>
          <p className="text-muted-foreground">
            We couldn't find the order you're looking for. <br />
            It may have been deleted or never existed.
          </p>
        </div>
      </CardContent>
      <CardFooter className="flex justify-center mb-6">
        <Link href="/">
          <Button variant="outline">Return to Home</Button>
        </Link>
      </CardFooter>
    </Card>
  )
}

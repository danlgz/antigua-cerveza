import { Card, CardContent, CardFooter } from "@/components/ui/card"
import { Skeleton } from "@/components/ui/skeleton"

function BeerAvatarSkeleton() {
  return (
    <Skeleton className="h-16 w-9 rounded-sm" />
  )
}

export default function OrderCardSkeleton() {
  return (
    <Card className="w-full">
      <CardContent className="flex justify-between items-top pt-8">
        <div>
          <Skeleton className="h-4 w-24 mb-3" />
          <Skeleton className="h-12 w-36 mb-3" />
          <Skeleton className="h-3 w-32 mb-1" />
          <Skeleton className="h-3 w-32" />
        </div>
        <div className="flex flex-col items-end">
          <Skeleton className="h-4 w-28 mb-2" />
          <div className="flex gap-2 overflow-hidden justify-end">
            <BeerAvatarSkeleton />
            <BeerAvatarSkeleton />
            <BeerAvatarSkeleton />
          </div>
        </div>
      </CardContent>
      <CardFooter className="flex justify-end mb-2">
        <Skeleton className="h-9 w-24" />
      </CardFooter>
    </Card>
  )
}

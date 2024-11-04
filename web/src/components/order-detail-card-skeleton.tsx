import { Card, CardContent, CardFooter } from "@/components/ui/card"
import { Skeleton } from "@/components/ui/skeleton"

function OrderItemCardSkeleton() {
  return (
    <Card className="w-full flex items-center shadow-none">
      <CardContent className="flex justify-between items-center py-4 px-8 w-full">
        <div className="flex gap-4 items-center">
          <Skeleton className="h-16 w-16 rounded" />
          <div>
            <Skeleton className="h-6 w-32 mb-1" />
            <Skeleton className="h-4 w-24 mb-1" />
            <Skeleton className="h-4 w-28" />
          </div>
        </div>
        <div>
          <Skeleton className="h-4 w-12 mb-1 ml-auto" />
          <Skeleton className="h-8 w-20" />
        </div>
      </CardContent>
    </Card>
  )
}

export default function OrderDetailCardSkeleton() {
  return (
    <Card className="w-full">
      <CardContent className="flex flex-col items-top pt-8 gap-8">
        <div className="flex flex-col items-center gap-4">
          <Skeleton className="h-4 w-24" />
          <Skeleton className="h-12 w-32" />

          <div className="flex gap-3 justify-center">
            <Skeleton className="h-3 w-24" />
            <Skeleton className="h-3 w-28" />
          </div>

          <Skeleton className="h-6 w-20 rounded-full" />
        </div>

        <div className="flex justify-center w-full">
          <div className="flex flex-col items-center w-full gap-4">
            <Skeleton className="h-10 w-64" /> {/* Skeleton for tabs */}
            <div className="w-full flex flex-col gap-4 mt-4">
              {[...Array(2)].map((_, index) => (
                <OrderItemCardSkeleton key={index} />
              ))}
            </div>
          </div>
        </div>
      </CardContent>
      <CardFooter className="flex flex-col justify-center mb-2 mt-4 items-center w-full">
        <div className="w-full text-right text-sm">
          <Skeleton className="h-4 w-24 ml-auto mb-1" />
          <Skeleton className="h-4 w-20 ml-auto mb-1" />
          <Skeleton className="h-4 w-28 ml-auto mb-1" />
          <Skeleton className="h-5 w-32 ml-auto my-2" />
        </div>
        <Skeleton className="h-10 w-24 mt-2" /> {/* Skeleton for "Go back" button */}
      </CardFooter>
    </Card>
  )
}

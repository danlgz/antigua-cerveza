import OrderCardSkeleton from "@/components/order-card-skeleton";

export default function Loading() {
  return (
    <div className="flex flex-col gap-4">
      {
        [...Array(10)].map((i) => <OrderCardSkeleton key={i} />)
      }
    </div>
  )
}

import OrderCardSkeleton from "@/components/order-card-skeleton";

export default function Loading() {
  return (
    <div className="flex flex-col gap-4">
      {
        [1, 2, 3, 4, 5, 6].map((i) => <OrderCardSkeleton key={i} />)
      }
    </div>
  )
}

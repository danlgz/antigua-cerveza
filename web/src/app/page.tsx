import OrderCard from "@/components/order-card";
import OrderCardSkeleton from "@/components/order-card-skeleton";


export default function Home() {
  return (
    <div className="flex flex-col gap-4 mb-4">
      <OrderCard />
      <OrderCardSkeleton />
      <OrderCardSkeleton />
      <OrderCardSkeleton />
      <OrderCardSkeleton />
    </div>
  );
}

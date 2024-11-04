'use server'

import { Order } from "@/types/order";
import makeRequest from '@/lib/http';

export default async function retrieveOrder(id: string) {
  return makeRequest<Order>(`/api/v1/orders/${id}`)
}

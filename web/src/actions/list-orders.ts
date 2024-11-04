'use server'

import camelcaseKeys from 'camelcase-keys';
import { Order } from "@/types/order";

export default async function listOrders() {
  const response = await fetch(`${process.env.API_HOST}/api/v1/orders`)
  return camelcaseKeys(await response.json(), { deep: true }) as Order[];
}

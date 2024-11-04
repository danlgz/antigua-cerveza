'use server'

import makeRequest from "@/lib/http";
import { BeerStock } from "@/types/beer-stock";

export default async function listBeersStock(ids: string[]) {
  const params = new URLSearchParams()
  ids.forEach(id => params.append('id', id))

  return makeRequest<BeerStock[]>(`/api/v1/beers-stock?${params}`)
}

'use server'

import { BeerStock } from "@/types/beer-stock";
import camelcaseKeys from "camelcase-keys";

export default async function listBeersStock(ids: string[]) {
  const params = new URLSearchParams()
  ids.forEach(id => params.append('id', id))

  const response = await fetch(`${process.env.API_HOST}/api/v1/beers-stock?${params}`)
  return camelcaseKeys(await response.json(), { deep: true }) as BeerStock[];
}

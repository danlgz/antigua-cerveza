'use server'

export async function listBeers(ids: string[]) {
  const params = new URLSearchParams()
  ids.forEach(id => params.append('id', id))

  const response = await fetch(`${process.env.API_HOST}/api/v1/orders?${params}`)
  return response.json()
}

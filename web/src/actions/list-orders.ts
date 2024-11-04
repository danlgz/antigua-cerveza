'use server'

export async function listOrders() {
  const response = await fetch(`${process.env.API_HOST}/api/v1/orders`)
  return response.json()
}

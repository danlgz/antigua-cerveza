export interface Order {
  id: string;
  paid: boolean;
  total: number;
  subtotal: number;
  taxes: number;
  discounts: number;
  items: OrderItem[];
  rounds: OrderRound[];
}

export interface OrderItem {
  beerStockId: string;
  pricePerUnit: number;
  total: number;
  quantity: number;
}

export interface OrderRound {
  created: string;
  items: OrderRoundItem[];
}

export interface OrderRoundItem {
  beerStockId: string;
  quantity: number;
}

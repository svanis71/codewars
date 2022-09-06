import { fact } from './factorial';

export function n_over_k(n, k) {
  return fact(n) / (fact(k) * fact(n - k));
}


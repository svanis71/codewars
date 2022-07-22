export const minDistance = (n) => {
    const factors = [1, n];
    const isEven = n % 2 === 0;
    const startidx =  isEven ? 2 : 3;
    const step = isEven ? 1 : 2;
    for(let i = startidx; i <= n / 2; i += step) {
        if(n % i == 0) {
            factors.push(i);
        }
    }
    factors.sort((a,b)=>b-a);
    return factors.reduce((p, c, idx, factors) => idx<factors.length-1?(c-factors[idx+1]>p?p:c-factors[idx+1]):p, n);
}
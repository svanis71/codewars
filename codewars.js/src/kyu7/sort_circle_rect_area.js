export function sortByArea(array) {
    const areas = array.map(x => +(Array.isArray(x) ? x[0] * x[1] : Math.PI * x * x).toFixed(2));
    return areas.sort((a, b) => a - b);
}
const arrayToString = function(a) {
    let res = '[';
    for(const item of a) {
        if(res.length > 1) {
            res += ',';
        }
        switch(typeof(item)) {
            case 'string':
                res += ('\'' + item + '\'');
                break;
            case 'number':
            case 'boolean':
                res += item;
                break;
            default: 
                if(Array.isArray(item)) {
                    res += arrayToString(item);
                }
        }
    }
    res += ']';
    return res;
};

export function arrayStringPrototype() {
    return arrayToString(this);
}

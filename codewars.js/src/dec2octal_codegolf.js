// f=x=>+(+x&7);

function dec2Oct(x) {
    return parseInt(parseInt(x).toString("8"));
}

module.exports = dec2Oct;
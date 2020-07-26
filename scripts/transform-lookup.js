const fs = require('fs');

const json = fs.readFileSync('./PeriodicTableJSON.json');

const Periodic = JSON.parse(json).elements;

const lookup = Periodic.reduce((acc, curr) => {
    const name = curr.name.toLowerCase();
    acc.order.push(name);
    acc[name] = curr;
    return acc;
}, { order: [] });

if(!!lookup.order.length) {
    fs.writeFile('./periodic-table-lookup.json', JSON.stringify(lookup, null, 4), () => {
        console.log('Periodic lookup successfully created');
    })
} else {
    throw new Error('Problem creating lookup file');
}

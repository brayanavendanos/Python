function Fibonacci (n) {
    let siguiente = 2;
    let fibonacci = [0, 1];

    while ( siguiente < Number(n) ) {
        
        let suma = Number(fibonacci[ siguiente - 2 ] + fibonacci[ siguiente - 1 ]);
        fibonacci.push(suma);
        siguiente++;
    }
    
    for (let i = 0; i < fibonacci.length; i++) {
        const element = fibonacci[i];
        console.log(`Iteración número ${i} : ${element}`);
    }
}

const cantidad = prompt('Cantidad de números');
Fibonacci(cantidad);
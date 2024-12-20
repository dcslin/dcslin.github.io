# Rust lang

## Basic Syntax

```rust
fn main() {
    const THREE_HOURS_IN_SECONDS: u32 = 60 * 60 * 3;

    let mut x = 5;
    println!("x is {x}");
    x = 6;
    println!("x is {x}");

    let guess:u32 = "42".parse().expect("failed to parse")

    let x = 2.0; // f64

    let y: f32 = 3.0; // f32

    let tup = (500, 6.4, 1);

    let (x, y, z) = tup;

    let x: (i32, f64, u8) = (500, 6.4, 1);

    let five_hundred = x.0;

    let six_point_four = x.1;

    let one = x.2;

    let a = [1, 2, 3, 4, 5];

    let a: [i32; 5] = [1, 2, 3, 4, 5];

    let a = [3; 5];

    if number < 5 {
        println!("condition was true");
    } else {
        println!("condition was false");
    }

    let number = if condition { 5 } else { 6 };

    loop {
        println!("again!");
        break;
    }

    while number != 0 {
        println!("{number}!");

        number -= 1;
    }

    let a = [10, 20, 30, 40, 50];

    for element in a {
        println!("the value is: {element}");
    }

    for number in (1..4).rev() {
        println!("{number}!");
    }
    println!("LIFTOFF!!!");
}

fn another_function(x: i32) {
    println!("The value of x is: {x}");
}

fn five() -> i32 {
    5
}

```

## Primitive Types, Collections

string, tuple, vector

```rust
let s = "hello";

let s = String::from("hello");



```

## Unique Concepts

Ownership, Reference, borrowing, pattern matching, Stack and Heap, Result and Panic, Traits, Lifetimes, smart pointers

## Other Core Concepts

Generics, enum, Closures, Iterators, struct, threading, oop


## Build Tools
Cargo, workspace, project structure, tests

```sh
cargo new project0

cargo build

cargo run
```
# Rust lang

## Basic Syntax

```rust
fn main() {
    let x = 5;
    println!("x is {x}");
    x = 6;
    println!("x is {x}");

    let guess:u32 = "42".parse().expect("failed to parse")
}
```

## Unique Core Concepts

Ownership, Reference, borrowing, pattern matching, Stack and Heap, Result and Panic, Traits, Lifetimes, smart pointers

## Other Core Concepts

Generics, enum, Closures, Iterators, struct, threading

## Primitive Types, Collections

vector

## Build Tools

Cargo, workspace, project structure, tests